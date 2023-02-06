from django.urls import path
from . import views

urlpatterns = [
    path("paymentPath/", views.payment_home, name="pay-home"),
    path("webhook2/", views.payment_webhook, name="webhook"),
    path("vote-pending/", views.vote_pending, name="vote-pending"),
]
