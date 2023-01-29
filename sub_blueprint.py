from flask import Blueprint

sub_blueprint = Blueprint('Subdomain route', __name__)

@sub_blueprint.route('/', subdomain='subdomain')
def index():
    return "This is a subdomain blueprint"
