from flask import Blueprint
from todo_backend import api

todo_blueprint = Blueprint('todo_app', __name__, url_prefix='/')

todo_blueprint.add_url_rule('login', "login", api.login, methods=["POST"])