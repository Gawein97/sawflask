from flask import Flask
from snakeeyes.blueprints.page import page


def create_app(test_config=None):
    """Create Flask application with factory pattern"""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py_production_example", silent=True)

    app.register_blueprint(page)

    return app
