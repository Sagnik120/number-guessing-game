import os
from dotenv import load_dotenv

# load your .env file
load_dotenv(dotenv_path="D:/project/Website/Number_gussing_game/.env")
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-in-production')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
