"""
Base webhook implementation
"""

from django.http import HttpResponse
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class WebhookBase(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WebhookBase, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        meta = copy.copy(request.META)

        for k, v in meta.items():
            if not isinstance(v, basestring):
                del meta[k]

        try:
            self.process_webhook(data, meta)
        except Exception:
            self.handle_exception()

        return HttpResponse(status=200)

    def process_webhook(self, data, meta):
        raise NotImplementedError
    
    def handle_exception(self, data, meta):
        pass
