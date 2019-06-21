from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    with app.app_context():
        from todo_backend.route import todo_blueprint
        app.register_blueprint(todo_blueprint)

    return app
