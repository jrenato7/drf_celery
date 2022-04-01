"""
This module create
"""
from django.urls import path

from .views import store_event

app_name = 'the_eye'

urlpatterns = [
    path(r'', store_event, name='event_save'),
]
