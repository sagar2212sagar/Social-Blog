# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-30 19:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
