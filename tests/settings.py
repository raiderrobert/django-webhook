"""
Testing mini-project and tests in one
"""

from __future__ import unicode_literals
import unittest

from django.conf import settings


if __name__ == '__main__':
    settings.configure()
    unittest.main()


DEBUG = True
ROOT_URLCONF = 'tests.urls'
DATABASES = {'default': {}}
SECRET_KEY = "not so secret"
