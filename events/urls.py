# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event-list'),
    path('<int:event_id>/', views.event_detail, name='event-detail'),
    path('favorite/<int:event_id>/', views.favorite_event, name='favorite-event'),
    path('unfavorite/<int:event_id>/', views.unfavorite_event, name='unfavorite-event'),
]