import pytest 

from hms.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    params = {
        "DEBUG" : False,
        "TESTING": True,
        'WTF_CSRF_ENABLED': False,
    }

    
    _app = create_app(settings_override=params)
    ctx = _app.app_context()

    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope="function")
def client(app):
    """
    Setting up an app client which is executed per finction
    """
    yield app.test_client()




