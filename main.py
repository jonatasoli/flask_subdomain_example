from flask import Flask

import config as default_config


def create_app(config=None) -> Flask:
    app = Flask(__name__, subdomain_matching=True)

    if config is None:
        config = default_config

    app.config.from_object(config)

    # Blueprints and API Namespaces
    from root_blueprint import main_blueprint
    app.register_blueprint(main_blueprint)
    from sub_blueprint import sub_blueprint
    app.register_blueprint(sub_blueprint)
    from dynamic_blueprint import dim_blueprint
    app.register_blueprint(dim_blueprint)
        
    # app = blueprints_factory.register_blueprints(app)


    return app
