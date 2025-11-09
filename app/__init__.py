from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Налаштування підключення до бази даних
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:dodkolox@database-1.clg8si4627g0.eu-north-1.rds.amazonaws.com/mydb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Налаштування Swagger
    app.config['SWAGGER'] = {
        'title': 'Database Lab 4 API',
        'uiversion': 3,
        'version': '1.0',
        'description': 'API documentation for Database Lab 4 project',
        'termsOfService': '',
        'contact': {
            'name': 'API Support',
            'email': 'support@example.com'
        }
    }

    # Ініціалізація Swagger
    Swagger(app)

    # Ініціалізація SQLAlchemy з додатком
    db.init_app(app)

    # Імпорт моделей для створення таблиць1
    from app.domains import models

    # Реєстрація Blueprint-ів
    from app.controller.objects_controller import objects_bp
    from app.controller.operators_controller import operators_bp
    from app.controller.rooms_controller import rooms_bp
    from app.controller.sensor_maintenance_controller import sensor_bp

    # Імпортуйте інші контролери аналогічно

    app.register_blueprint(objects_bp, url_prefix='/api')
    app.register_blueprint(operators_bp, url_prefix='/api')
    app.register_blueprint(rooms_bp, url_prefix='/api')
    app.register_blueprint(sensor_bp, url_prefix='/api')

    @app.route("/health", methods=["GET"])
    def health():
        return {"status": "ok"}, 200

    return app
