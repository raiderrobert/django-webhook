"""
Testing mini-project and tests in one
"""
from django.conf import settings
from django.test import TestCase
from django.test.client import Client

from django.conf.urls import url, include
settings.configure()

from webhook import WebhookBase

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


# Tests start here

class TestWebhook(TestCase):

  def setUp(self):
      """initialize the Django test client"""
      self.c = Client()
        
  def test_your_test(self):
      python_dict = {
          "eventId": "5c0007",
          "portalId": 999,
          "userEmail": "fake@email.com"
      }
      response = self.c.post('/webhook-receiver/',
                                  json.dumps(python_dict),
                                  content_type="application/json")

