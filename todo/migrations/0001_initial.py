# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default=b'', max_length=500)),
                ('desc', models.TextField(default=b'')),
                ('expected_time', models.CharField(default=b'', max_length=25)),
                ('minimum_timeslot', models.IntegerField(default=5, verbose_name=b'Minimum Timeslot')),
                ('status', models.CharField(default=b'active', max_length=25, choices=[(b'active', b'Active'), (b'done', b'Done'), (b'cancel', b'Cancel')])),
            ],
        ),
        migrations.AddField(
            model_name='tasklog',
            name='task',
            field=models.ForeignKey(to='todo.Todo'),
        ),
    ]
