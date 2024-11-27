# Generated by Django 5.1.3 on 2024-11-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0004_remove_tag_tag_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tag_category',
            field=models.CharField(choices=[('event_type', 'Event Type'), ('event_theme', 'Event Theme')], default='event_type', max_length=50),
        ),
    ]