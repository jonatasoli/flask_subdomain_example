import locale

from flask import Flask

import config as default_config


def create_app(config=None) -> Flask:
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")  # set locale
    app = Flask(__name__, static_folder="../static", template_folder="../templates")

    if config is None:
        config = default_config

    app.config.from_object(config)

    # Blueprints and API Namespaces
    from root_blueprint import main_blueprint
    app.register_blueprint(main_blueprint)
    from sub_blueprint import sub_blueprint
    app.register_blueprint(sub_blueprint)
        
    # app = blueprints_factory.register_blueprints(app)


    return app
