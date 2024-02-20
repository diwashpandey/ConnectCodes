# Generated by Django 5.0.2 on 2024-02-20 08:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_alter_message_room'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='room_members', to=settings.AUTH_USER_MODEL),
        ),
    ]