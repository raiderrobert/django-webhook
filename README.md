# django-webhook
Make webhooks in Django very quickly and easily.

##  Basic Implementation

The `WebhookBase` class is a simple implementation for consuming a webhook.

Make an app 

    # my_app/views
    
    from .models import YourModel
    
    
    class WebhookView(WebhookBase):
    
        def process_webhook(self, data, meta):
            YourModel.objects.create(
                event_name=data['webhookEvent'],
                body=data,
                request_meta=meta
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
          
