# users/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("User home page - Placeholder")