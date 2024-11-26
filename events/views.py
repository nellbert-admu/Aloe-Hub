# events/views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})