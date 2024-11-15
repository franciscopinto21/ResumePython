# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Instanciando o objeto SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa o banco de dados com a aplicação
    db.init_app(app)

    # Registra o blueprint
    from .views import main_bp
    app.register_blueprint(main_bp)

    return app
