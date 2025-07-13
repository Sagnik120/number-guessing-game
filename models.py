# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Leaderboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    level = db.Column(db.String(10), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow().date)
