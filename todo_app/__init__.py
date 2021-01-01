from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    register_blueprints(app)

    # Create sql tables for our data models
    # Found from this link.  https://hackersandslackers.com/flask-sqlalchemy-database-models/
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app


def register_blueprints(app):
    from todo_app.routes import routes
    app.register_blueprint(routes)
