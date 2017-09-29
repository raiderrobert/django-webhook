# django-webhook
Make webhooks in Django very quickly and easily.

[![Build Status](https://travis-ci.org/raiderrobert/django-webhook.svg?branch=master)](https://travis-ci.org/raiderrobert/django-webhook)
[![Coverage Status](https://coveralls.io/repos/github/raiderrobert/django-webhook/badge.svg?branch=master)](https://coveralls.io/github/raiderrobert/django-webhook?branch=master)

## Install via Pip

    pip install git+https://github.com/raiderrobert/django-webhook/

##  Basic Implementation

The `WebhookBase` class is a simple implementation for consuming a webhook.

Given a model

    # my_app/models
    from .models import YourModel
    
    
    class YourModel(models.Model):
        event_name = models.CharField(max_length=255)
        body = models.TextField()
    

And given a JSON payload

    {
        'webhookEvent':'boom',
        'numThing': 1,
        'charThing': 'foo'
    }

Make an app 

    # my_app/views
    from webhook.base import WebhookBase
    from .models import YourModel
    
    
    class WebhookView(WebhookBase):
    
        def process_webhook(self, data):
            YourModel.objects.create(
                event_name=data['webhookEvent'],
                body=data
            )


Hook it into your urls.

    # my_project/urls
    
    from django.contrib import admin
    from django.conf.urls import url, include
    from my_app import views
    
    
    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^webhook-receiver', views.WebhookView.as_view(), name='web_hook'),
    ]
          
