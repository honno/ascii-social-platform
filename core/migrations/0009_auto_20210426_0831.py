# Generated by Django 3.1.7 on 2021-04-26 08:31

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_auto_20210426_0828"),
    ]

    operations = [
        migrations.AlterField(
            model_name="art",
            name="thumb_render",
            field=models.ImageField(default=None, upload_to="thumbs"),
        ),
    ]
