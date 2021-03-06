# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField()),
                ('intro', models.TextField()),
                ('content_link', models.URLField()),
                ('term', models.TextField()),
                ('date', models.DateField()),
                ('num_of_registered_participants', models.IntegerField(default=0)),
                ('num_of_actual_participants', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Workshop',
            },
        ),
    ]
