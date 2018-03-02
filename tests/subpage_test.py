# coidng: utf-8

import pytest


@pytest.fixture
def app():
    import main
    main.app.testing = True
    return main.app.test_client()


def test_index(app):
    r = app.get('/subpage')
    assert r.status_code == 200
