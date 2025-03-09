"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page to show all topics
    path('topics/', views.topics, name='topics'),
    # Show the details of a certain topic
    path(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic')
]