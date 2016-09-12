from django.conf.urls import url, include
from webhook.base import WebhookBase


class WebhookView(WebhookBase):

    def process_webhook(self, data, meta):
        pass


urlpatterns = [
    url(r'^webhook-receiver', WebhookView.as_view(), name='web_hook'),
]
