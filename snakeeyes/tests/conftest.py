import pytest
from snakeeyes.app import create_app


@pytest.yield_fixture(scope="session")
def app():
    """
    Setup test Flask app only executes once
    :return: Flask app
    """
    params = {
        "DEBUG": False,
        "TESTING": True
    }

    _app = create_app(params)
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope="function")
def client(app):
    """
    Setup flask app client, this gets execute at each test
    :param app: fixture
    :return: Flask app cient
    """
    yield app.test_client()
