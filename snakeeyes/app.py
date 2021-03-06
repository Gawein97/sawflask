from flask import Flask
from snakeeyes.blueprints.page import page
from snakeeyes.utils import inject_year_preproc
from snakeeyes.extensions import debug_toolbar


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
    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutate app passed in)

    :param app: Flask app instance
    :return: None
    """
    debug_toolbar.init_app(app)
    return None
