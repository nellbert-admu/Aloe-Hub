# events/views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Event
import time

def event_list(request):
    query = request.GET.get('q')
    events = Event.objects.all()
    
    if query:
        start_time = time.time()
        events = linear_search(events, query)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Linear Search Algorithm Analysis: O(n)")
        print(f"Time taken for search: {elapsed_time:.6f} seconds")
    
    # Sort events by date using Quick Sort
    start_time = time.time()
    events = quick_sort(events)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Quick Sort Algorithm Analysis: O(n log n)")
    print(f"Time taken for sorting: {elapsed_time:.6f} seconds")

    return render(request, 'events/events.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def linear_search(events, query):
    # Linear search goes through each event one by one and checks if the query is in the title or description.
    result = []
    for event in events:
        if query.lower() in event.title.lower() or query.lower() in event.description.lower():
            result.append(event)
    return result

def quick_sort(events):
    # Quick sort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element from the array
    # and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
    if len(events) <= 1:
        return events
    pivot = events[len(events) // 2]
    left = [x for x in events if x.date < pivot.date]
    middle = [x for x in events if x.date == pivot.date]
    right = [x for x in events if x.date > pivot.date]
    return quick_sort(left) + middle + quick_sort(right)