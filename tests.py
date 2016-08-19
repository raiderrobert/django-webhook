import simplejson

from django.conf import settings
from django.test import TestCase
from django.test.client import Client

from webhook import WebhookBase


DEBUG = True
ROOT_URLCONF = 'tests'
DATABASES = {'default': {}}
SECRET_KEY = "not so secret"

urlpatterns = [
    url(r'^webhook-receiver', WebhookView.as_view(), name='web_hook'),
]


class WebhookView(WebhookBase):

    def process_webhook(self, data, meta):
        pass


class TestPipeline(TestCase):

  def setUp(self):
      """initialize the Django test client"""
      self.c = Client()
        
  def test_your_test(self):
      python_dict = {
          "1": {
              "guid": "8a40135230f21bdb0130f21c255c0007",
              "portalId": 999,
              "email": "fake@email"
          }
      }
      response = self.c.post('/webhook-receiver/',
                                  json.dumps(python_dict),
                                  content_type="application/json")

