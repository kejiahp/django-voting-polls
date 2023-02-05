from django.urls import path
from . import views

urlpatterns = [
    path("paymentPath/", views.payment_home, name="pay-home"),
    path("webhook/", views.payment_webhook, name="webhook"),
    path("webhook2/", views.payment_test, name="webhook-test"),
]
