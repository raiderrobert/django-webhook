"""
Base webhook implementation
"""
import json

from django.http import HttpResponse
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class WebhookBase(View):
    """
    Simple Webhook base class to handle the most standard case.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WebhookBase, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))
        self.process_webhook(data)
        return HttpResponse(status=200)

    def process_webhook(self, data):
        raise NotImplementedError
