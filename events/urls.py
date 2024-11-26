# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event-list'),
    path('<int:event_id>/', views.event_detail, name='event-detail'),
]