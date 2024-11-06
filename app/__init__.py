from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Налаштування підключення до бази даних
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/mydb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ініціалізація SQLAlchemy з додатком
    db.init_app(app)

    # Імпорт моделей для створення таблиць
    from app.domains import models

    # Реєстрація Blueprint-ів
    from app.controller.objects_controller import objects_bp
    from app.controller.operators_controller import operators_bp
    from app.controller.rooms_controller import rooms_bp
    # Імпортуйте інші контролери аналогічно

    app.register_blueprint(objects_bp, url_prefix='/api')
    app.register_blueprint(operators_bp, url_prefix='/api')
    app.register_blueprint(rooms_bp, url_prefix='/api')
    # Реєструйте інші Blueprint-и аналогічно

    return app
