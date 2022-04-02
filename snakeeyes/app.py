from flask import Flask


def create_app(test_config=None):
    """Create Flask application with factory pattern"""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    @app.route("/")
    def index():
        """response from home page"""
        return "Hello World"

    return app
