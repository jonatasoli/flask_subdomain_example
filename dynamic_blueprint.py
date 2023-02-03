from flask import Blueprint

dim_blueprint = Blueprint('Dynamic Subdomain route', __name__)


@dim_blueprint.route('/', subdomain='<username>')
def dynamic(username):
    return f'This is a {username} blueprint'
