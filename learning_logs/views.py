from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """ The Home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """ The page that show all the topics """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ The page that shows the details of a topic """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {"Topic": topic, "Entries": entries}
    return render(request, 'learning_logs/topic.html', context)
