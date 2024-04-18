import pytest
from flask import template_rendered
from app import application


@pytest.fixture
def client():
    with application.test_client() as client:
        yield client


def test_root_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"index.html" in response.data


def test_help_route(client):
    response = client.get("/help")
    assert response.status_code == 200
    assert b"help.html" in response.data


def test_hello_route(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert b"Hello World from Flask Hello Page.<b> v1.0" in response.data


def test_template_rendering(client):
    templates = []

    def capture_template(sender, template, context, **extra):
        templates.append(template.name)

    template_rendered.connect(capture_template, application)

    client.get("/")
    client.get("/help")
    client.get("/hello")

    assert "index.html" in templates
    assert "help.html" in templates