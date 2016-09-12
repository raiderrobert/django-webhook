from __future__ import absolute_import
from __future__ import unicode_literals

import json

from django.test import TestCase
from django.test.client import Client


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
        self.assertEqual(response.status_code, 200)
