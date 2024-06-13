from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from .auth import auth_bp
from .routes import api_bp

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('instance.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Bookstore API"})
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
