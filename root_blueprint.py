from flask import Blueprint

main_blueprint = Blueprint('Root route', __name__)

@main_blueprint.route('/')
def index():
    return "This is a main blueprint"
