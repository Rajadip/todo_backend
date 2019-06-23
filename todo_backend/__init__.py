from flask import Flask
from todo_backend.extension import *


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    cors.init_app(app=app)
    with app.app_context():
        from todo_backend.route import todo_blueprint
        app.register_blueprint(todo_blueprint)

    return app
