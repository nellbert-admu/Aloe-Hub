from django.db import models

class Event(models.Model):
    PARTICIPATION_CHOICES = [
        ('everyone', 'Everyone'),
        ('members', 'Members Only'),
        ('ateneans', 'Ateneans Only'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    participation = models.CharField(max_length=10, choices=PARTICIPATION_CHOICES, default='everyone')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
