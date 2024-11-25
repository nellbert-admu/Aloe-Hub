# events/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Event home page - Placeholder")