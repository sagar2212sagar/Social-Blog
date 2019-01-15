# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-06 21:48
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_posts_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, upload_to=blog.models.upload_location),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
