import pytest
from flask import url_for
from flask_testing import TestCase

from app import application

class TestBase(TestCase):
    def create_app(self):
        return application

class TestRoutes(TestBase):
    def test_root_route(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert b"This is my Assignment Task!" in response.data # Updated assertion

    def test_help_route(self):
        response = self.client.get("/help")
        assert response.status_code == 200
        assert b"THIS IS HELP PAGE" in response.data # Updated assertion

    def test_hello(self):
        response = self.client.get("/hello")
        self.assert200(response)
        self.assertEqual(response.data.decode(), "Hello World from Flask Hello Page.<b> v1.0")
