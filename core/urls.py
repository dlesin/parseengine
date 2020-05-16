from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home_view_url'),
    path('contacts/', ContactView.as_view(), name='contacts_view_url'),
]
