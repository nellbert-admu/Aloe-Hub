# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event-list'),
    path('<int:event_id>/', views.event_detail, name='event-detail'),
    path('save/<int:event_id>/', views.save_event, name='save-event'),
    path('unsave/<int:event_id>/', views.unsave_event, name='unsave-event'),
    path('favorite/<int:event_id>/', views.favorite_event, name='favorite-event'),
    path('unfavorite/<int:event_id>/', views.unfavorite_event, name='unfavorite-event'),
]