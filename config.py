import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Assumindo que você tenha a variável de ambiente DATABASE_URL configurada
    SQLALCHEMY_TRACK_MODIFICATIONS = False

