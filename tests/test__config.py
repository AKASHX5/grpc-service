
import unittest

from flask import current_app
from flask_testing import TestCase

# from project.server import app
import webapp

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        webapp.config.from_object('project.server.config.DevelopmentConfig')
        return webapp

    def test_app_is_development(self):
        self.assertTrue(webapp.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            webapp.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/flask_jwt_auth'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        webapp.config.from_object('project.server.config.TestingConfig')
        return webapp

    def test_app_is_testing(self):
        self.assertTrue(webapp.config['DEBUG'])
        self.assertTrue(
            webapp.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:@localhost/flask_jwt_auth_test'
        )