# 🎯 Number Guessing Game

A fun web-based Number Guessing Game built with **Flask**, where users can pick difficulty levels, guess random numbers, and view a persistent leaderboard stored in a PostgreSQL database.

---

## 🚀 Features

✅ **Difficulty Levels**
- Easy → 1-10 (unlimited tries)
- Medium → 1-50 (7 tries)
- Hard → 1-100 (5 tries)

✅ **Leaderboard**
- Stores player names, levels, scores, dates.
- Displays top scores in descending order.

✅ **Modern UI**
- Built with Bootstrap for responsive design.
- Custom styling and background images.

✅ **Security**
- Environment variables used for secrets and DB configs.
- User sessions protected with Flask’s secret key.

---

## 🖼️ Screenshots

Example:


### Home Page
![Home](images/home.png)

### Game Page
![Game](images/game.png)

### Result Page
![Result](images/win.png)

### Leaderboard
![Leaderboard](images/leaderboard.png)

---

## 🛠️ Tech Stack

- **Flask** (Python web framework)
- **Flask SQLAlchemy** (ORM)
- **PostgreSQL** (Database)
- **Bootstrap 5** (Frontend styling)
- **HTML** (Frontend)
- **CSS** (Frontend styling)
- **JS** (Frontend styling)
- **dotenv** (Environment variable management)

---

## 📂 Project Structure

NUMBER_GUESSING_GAME/
│
├── static/
│ ├── css/
│ │ └── styles.css
│ ├── images/
│ │ ├── home.jpg
│ │ ├── game.jpg
│ │ ├── result.jpg
│ │ ├── leaderboard.jpg
│ │ └── confetti.gif
│ └── js/
│
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── game.html
│ ├── result.html
│ └── leaderboard.html
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── .env
└── .gitignore


## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/number-guessing-game.git
cd number-guessing-game

### 2. Create Virtual Environment
Recommended:
python -m venv venv
source venv/bin/activate         # macOS/Linux
venv\Scripts\activate            # Windows


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Set Environment Variables
Create a .env file in the root folder:
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/numbergame



### 5. Setup Database
Ensure PostgreSQL is running and your DB exists. Then:
# Run once (in Python shell) to create tables:
from app import db, app
with app.app_context():
    db.create_all()


### 6. Run the App
flask run
Visit: http://127.0.0.1:5000/


