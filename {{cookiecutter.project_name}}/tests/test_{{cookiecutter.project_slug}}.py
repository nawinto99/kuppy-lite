import pytest

from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}


@pytest.fixture
def client():
    with {{cookiecutter.project_slug}}.app.test_client() as client:
        yield client


def test_hello(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
