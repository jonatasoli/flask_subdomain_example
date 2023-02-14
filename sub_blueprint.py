from flask import Blueprint, redirect
from functools import partial

FIRST_DOMAIN = "myfinances.guru"
SECOND_DOMAIN = "taurusbrothers.pro"
sub_blueprint = Blueprint('Subdomain route', __name__)
second = Blueprint('second', __name__)
second_route = partial(second.route, host=SECOND_DOMAIN)



@sub_blueprint.route('/', subdomain='subdomain')
def index():
    return 'This is a subdomain blueprint'


@second_route('/')
def second_index():
    return redirect(f'http://angelica.{FIRST_DOMAIN}')
