from django.db import models

class Tag(models.Model):
    TAG_CATEGORIES = [
        ('event_type', 'Event Type'),
        ('event_theme', 'Event Theme'),
    ]

    name = models.CharField(max_length=50, unique=True)
    tag_category = models.CharField(
        max_length=50,
        choices=TAG_CATEGORIES,
        default='event_type',
    )
    

    def __str__(self):
        return self.name
# Create your models here.
