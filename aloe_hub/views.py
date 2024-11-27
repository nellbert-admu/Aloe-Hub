
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def event_list(request):
    # Your logic for listing events
    return render(request, 'events.html')

def event_detail(request, id):
    # Your logic for event details
    return render(request, 'event_detail.html')

def about(request):
    return render(request, 'about.html')