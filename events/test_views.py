from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event
from organizations.models import Organization
from tags.models import Tag
from datetime import datetime, time

# events/test_views.py


class EventViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.organization = Organization.objects.create(name='Test Organization')
        self.tag1 = Tag.objects.create(name='Conference', tag_category='event_type')
        self.tag2 = Tag.objects.create(name='Workshop', tag_category='event_theme')
        self.event = Event.objects.create(
            title='Test Event',
            location='Test Location',
            date=datetime.now().date(),
            time=datetime.now().time(),
            participation='Online',
            organized_by=self.organization
        )
        self.event.tags.add(self.tag1, self.tag2)

    def test_event_list_view(self):
        response = self.client.get(reverse('event-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertIn('events', response.context)
        self.assertIn('event_type_tags', response.context)
        self.assertIn('event_theme_tags', response.context)
        self.assertIn('organizations', response.context)

    def test_event_detail_view(self):
        response = self.client.get(reverse('event-detail', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_detail.html')
        self.assertEqual(response.context['event'], self.event)

    def test_favorite_event_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('favorite-event', args=[self.event.id]), {'event_id': self.event.id})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.event.favorited_by.filter(id=self.user.id).exists())

    def test_unfavorite_event_view(self):
        self.client.login(username='testuser', password='12345')
        self.event.favorited_by.add(self.user)
        response = self.client.post(reverse('unfavorite-event', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.event.favorited_by.filter(id=self.user.id).exists())

    def test_filter_by_event_type(self):
        response = self.client.get(reverse('event-list'), {'event_type': 'Conference'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.event, response.context['events'])

    def test_filter_by_event_themes(self):
        response = self.client.get(reverse('event-list'), {'event_themes': ['Workshop']})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.event, response.context['events'])

    def test_filter_by_location(self):
        response = self.client.get(reverse('event-list'), {'location': 'Test Location'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.event, response.context['events'])

    def test_filter_by_participation(self):
        response = self.client.get(reverse('event-list'), {'participation': 'Online'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.event, response.context['events'])

    def test_filter_by_time_after(self):
        response = self.client.get(reverse('event-list'), {'time_after': '00:00'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.event, response.context['events'])

    def test_filter_by_organization(self):
        response = self.client.get(reverse('event-list'), {'organization': 'Test Organization'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.event, response.context['events'])