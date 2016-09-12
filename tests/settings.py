"""
Testing mini-project and tests in one
"""

from __future__ import unicode_literals
from django.conf import settings


DEBUG = True
ROOT_URLCONF = 'tests.urls'
SECRET_KEY = "not so secret"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}
