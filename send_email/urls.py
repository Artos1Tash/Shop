from django.urls import path
from send_email.views import SendView


urlpatterns = [
    path('send/', SendView.as_view())
]
