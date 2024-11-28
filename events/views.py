# events/views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
import time
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import FavoriteEventForm

def event_list(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort_by', 'date')
    events = Event.objects.all()  # QuerySet

    # Apply filters
    if 'event_type' in request.GET and request.GET['event_type']:
        events = events.filter(event_type=request.GET['event_type'])  # QuerySet
    if 'time_after' in request.GET and request.GET['time_after']:
        events = events.filter(time__gte=request.GET['time_after'])  # QuerySet
    if 'location' in request.GET and request.GET['location']:
        events = events.filter(location__icontains(request.GET['location']))  # QuerySet
    if 'tags' in request.GET and request.GET['tags']:
        tags = [tag.strip() for tag in request.GET['tags'].split(',')]  # List
        events = events.filter(tags__name__in=tags).distinct()  # QuerySet
    if 'participation' in request.GET and request.GET['participation']:
        events = events.filter(participation=request.GET['participation'])  # QuerySet
    
    if query:
        start_time = time.time()
        events = linear_search(events, query)  # List
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Linear Search Algorithm Analysis")
        print(f"Time taken for search: {elapsed_time:.6f} seconds")
        print(f"Space complexity for search: O(n)")
    
    # Sort events by the selected category using Quick Sort
    start_time = time.time()
    events = quick_sort(events, sort_by)  # List
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Quick Sort Algorithm Analysis")
    print(f"Time taken for sorting: {elapsed_time:.6f} seconds")
    print(f"Space complexity for sorting: O(n log n)")

    return render(request, 'events/events.html', {'events': events})  # Dictionary

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Event instance
    return render(request, 'events/event_detail.html', {'event': event})  # Dictionary

def linear_search(events, query):
    # Linear search goes through each event title one by one and checks if the query is in the title.
    result = []  # List
    for event in events:
        if query.lower() in event.title.lower():
            result.append(event)
    return result  # List

def quick_sort(events, sort_by):
    if len(events) <= 1:
        return events  # List
    pivot = events[len(events) // 2]  # Event instance
    
    # Dictionary mapping sort_by values to lambda functions
    key_func = {
        'title': lambda x: x.title,  # Sort by title
        'location': lambda x: x.location,  # Sort by location
        'date': lambda x: x.date  # Sort by date
    }.get(sort_by, lambda x: x.date)  # Default to sorting by date if sort_by is not found
    
    left = [x for x in events if key_func(x) < key_func(pivot)]  # List
    middle = [x for x in events if key_func(x) == key_func(pivot)]  # List
    right = [x for x in events if key_func(x) > key_func(pivot)]  # List
    
    return quick_sort(left, sort_by) + middle + quick_sort(right, sort_by)  # List

@login_required
def favorite_event(request, event_id):
    if request.method == 'POST':
        form = FavoriteEventForm(request.POST)  # FavoriteEventForm instance
        if form.is_valid():
            event = get_object_or_404(Event, id=form.cleaned_data['event_id'])  # Event instance
            if request.user in event.favorited_by.all():  # QuerySet
                event.favorited_by.remove(request.user)
                favorited = False
                print(f"User {request.user.username} unfavorited event {event.title}")
            else:
                event.favorited_by.add(request.user)
                favorited = True
                print(f"User {request.user.username} favorited event {event.title}")
            return redirect('event-detail', event_id=event.id)
    return JsonResponse({'error': 'Invalid request'}, status=400)  # Dictionary

@login_required
def unfavorite_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Event instance
    event.favorited_by.remove(request.user)
    return JsonResponse({'unfavorited': True})  # Dictionary