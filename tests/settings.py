"""
Testing mini-project and tests in one
"""

from __future__ import unicode_literals
import unittest

from django.conf import settings
from django.test import TestCase
from django.test.client import Client

from django.conf.urls import url, include

if __name__ == '__main__':
    settings.configure()
    unittest.main()

from webhook.base import WebhookBase

# Mini Project starts here

DEBUG = True
ROOT_URLCONF = 'tests'
DATABASES = {'default': {}}
SECRET_KEY = "not so secret"


class WebhookView(WebhookBase):

    def process_webhook(self, data, meta):
        pass


urlpatterns = [
    url(r'^webhook-receiver', WebhookView.as_view(), name='web_hook'),
]
