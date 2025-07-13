from flask import Flask, render_template, request, session, redirect, url_for
from models import db, Leaderboard
from config import Config
import random
from sqlalchemy import desc
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# ✅ FIXED: Create tables with app context, not decorator
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/start', methods=['POST'])
def start():
    name = request.form.get('name', '').strip()

    if not name:
        return redirect(url_for('home'))

    level = request.form['level']
    if level == 'easy':
        number = random.randint(1,10)
        max_guesses = None
    elif level == 'medium':
        number = random.randint(1,50)
        max_guesses = 7
    else:
        number = random.randint(1,100)
        max_guesses = 5

    session['player_name'] = name
    session['number'] = number
    session['guesses'] = 0
    session['max_guesses'] = max_guesses
    session['level'] = level

    return redirect(url_for('game'))

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        guess = int(request.form['guess'])
        number = session['number']
        session['guesses'] += 1
        max_guesses = session['max_guesses']

        if guess == number:
            score = calculate_score(session['level'], session['guesses'])
            return redirect(url_for('result', status='win', score=score))
        else:
            hint = 'Try higher!' if guess < number else 'Try lower!'

            if max_guesses and session['guesses'] >= max_guesses:
                return redirect(url_for('result', status='lose', score=0))

            return render_template(
                'game.html',
                hint=hint,
                guesses=session['guesses'],
                max_guesses=max_guesses
            )

    return render_template(
        'game.html',
        hint=None,
        guesses=session.get('guesses', 0),
        max_guesses=session.get('max_guesses', None)
    )

@app.route('/result/<status>')
def result(status):
    number = session['number']
    score = int(request.args.get('score', 0))
    return render_template('result.html', status=status, number=number, score=score)

@app.route('/save_score', methods=['POST'])
def save_score():
    score = int(request.form['score'])
    level = session.get('level', 'unknown')
    name = session.get('player_name', None)

    if not name:
        return redirect(url_for('home'))

    new_entry = Leaderboard(
        player_name=name,
        score=score,
        level=level,
        date=datetime.utcnow().date()
    )
    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('leaderboard'))


@app.route('/leaderboard')
def leaderboard():
    today = datetime.utcnow().date()
    seven_days_ago = today - timedelta(days=7)

    # get all entries from last 7 days
    entries = (
        Leaderboard.query
        .filter(Leaderboard.date >= seven_days_ago)
        .order_by(Leaderboard.date.desc(), Leaderboard.score.desc())
        .all()
    )

    # group entries by date
    grouped_entries = {}
    for entry in entries:
        grouped_entries.setdefault(entry.date, []).append(entry)

    # sort groups by date descending
    sorted_grouped = sorted(grouped_entries.items(), key=lambda x: x[0], reverse=True)

    return render_template(
        'leaderboard.html',
        grouped_entries=sorted_grouped,
        today=today
    )


def calculate_score(level, guesses):
    base_score = {
        'easy': 50,
        'medium': 100,
        'hard': 150
    }.get(level, 0)

    # exponential decay factor
    penalty_factor = 0.85
    score = base_score * (penalty_factor ** (guesses - 1))

    return int(max(score, 0))

if __name__ == '__main__':
    app.run(debug=True)
