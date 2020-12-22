from flask import Flask


def create_app():
    app = Flask(__name__)
    from todo_app.routes import routes
    app.register_blueprint(routes)
    return app
