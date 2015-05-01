# -*- coding: utf-8 -*-
from django.db import models


class Todo(models.Model):
    created_at = models.DateTimeField( auto_now_add=True)
    modified_at = models.DateTimeField( auto_now_add=True)
    title = models.CharField(max_length=500, default="")
    desc = models.TextField(default="")

    #: the time needed for this item to be done.
    expected_time = models.CharField(max_length=25, default="")
    minimum_timeslot = models.IntegerField(verbose_name="Minimum Timeslot", default=5)
    status = models.CharField(max_length=25, 
        choices=(
            ("active", "Active"), 
            ("done", "Done"), 
            ("cancel", "Cancel")
        ),
        default="active"
    )

    def __unicode__(self):
        return "%d - %s - %s" % (self.pk, self.title, self.status,)


class TaskLog(models.Model):
    task = models.ForeignKey(Todo)
    created_at = models.DateTimeField(auto_now_add=True)
