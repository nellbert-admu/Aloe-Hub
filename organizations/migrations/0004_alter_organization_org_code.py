# Generated by Django 5.1.3 on 2024-11-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_organization_org_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='org_code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]