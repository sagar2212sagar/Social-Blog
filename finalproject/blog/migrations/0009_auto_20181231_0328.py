# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-30 21:58
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location),
        ),
    ]
