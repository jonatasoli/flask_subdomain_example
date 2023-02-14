from flask import Flask

import config as default_config

FIRST_DOMAIN = "myfinances.guru"
SECOND_DOMAIN = "taurusbrothers.pro"


def create_app(config=None) -> Flask:
    app = Flask(__name__, host_matching=True, subdomain_matching=True, static_folder='static', static_host=FIRST_DOMAIN)

    # if config is None:
    #     config = default_config

    # app.config.from_object(config)

    # Blueprints and API Namespaces
    from root_blueprint import main_blueprint
    app.register_blueprint(main_blueprint)

    from sub_blueprint import sub_blueprint
    app.register_blueprint(sub_blueprint)

    from sub_blueprint import second
    app.register_blueprint(second)

    from dynamic_blueprint import dim_blueprint
    app.register_blueprint(dim_blueprint)

    return app
