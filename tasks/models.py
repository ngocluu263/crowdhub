from __future__ import unicode_literals

from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
