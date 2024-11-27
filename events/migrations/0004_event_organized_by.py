# Generated by Django 5.1.3 on 2024-11-27 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_favorited_by'),
        ('organizations', '0002_organization_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organized_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organized_events', to='organizations.organization'),
        ),
    ]
