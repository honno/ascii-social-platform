# Generated by Django 3.1.7 on 2021-04-23 09:29

import uuid

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_art_thumb_render"),
    ]

    operations = [
        migrations.AddField(
            model_name="art",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
