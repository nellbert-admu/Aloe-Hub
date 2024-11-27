from django.db import models

class Organization(models.Model):
    COA = 'COA'
    LIONS = 'LIONS'
    OTHER = 'OTHER'
    
    CATEGORY_CHOICES = [
        (COA, 'COA'),
        (LIONS, 'LIONS'),
        (OTHER, 'Other'),
    ]

    org_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default=OTHER,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
