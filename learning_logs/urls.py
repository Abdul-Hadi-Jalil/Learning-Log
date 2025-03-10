""" Define the url patterns for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Topics page to show all topics
    path('topics/', views.topics, name='topics'),
    
    # Show the details of a certain topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # for users to add new topic page
    path('new_topic/', views.new_topic, name='new_topic'),

    # Entries for new topics
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry' )
]
