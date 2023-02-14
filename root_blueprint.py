from flask import Blueprint

main_blueprint = Blueprint('Root route', __name__)

FIRST_DOMAIN = "myfinances.guru"

@main_blueprint.route('/', host=FIRST_DOMAIN)
def index():
    return 'This is a main blueprint'
