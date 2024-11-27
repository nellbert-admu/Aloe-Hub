# Generated by Django 5.1.3 on 2024-11-27 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_organized_by'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(related_name='events', to='tags.tag'),
        ),
    ]
