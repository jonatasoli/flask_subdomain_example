from flask import Blueprint

dim_blueprint = Blueprint('Dynamic Subdomain route', __name__)
FIRST_DOMAIN = "myfinances.guru"


@dim_blueprint.route('/', subdomain='<username>', host=FIRST_DOMAIN)
def dynamic(username):
    return f'This is a {username} blueprint'
