import os
from flask_testing import TestCase
from api import create_app


class BaseTestCase(TestCase):

    def create_app(self):
        settings = os.environ.get('APP_SETTINGS', 'config.local.Development')
        app = create_app(settings)
        return app