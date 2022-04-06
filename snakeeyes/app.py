from flask import Flask
from snakeeyes.blueprints.page import page
from snakeeyes.utils import inject_year_preproc


def create_app(config_override=None):
    """
    Create Flask application with factory pattern

    :param: overrides configuration
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if config_override:
        app.config.update(config_override)

    app.register_blueprint(page)
    app.context_processor(inject_year_preproc)

    return app
