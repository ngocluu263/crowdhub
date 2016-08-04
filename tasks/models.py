from __future__ import unicode_literals

from django.db import models
from tasks.models_data import Item


class Protocol(models.Model):

    def create_task(self, task_name, parameters):
        task = Task(protocol=self, task_name=task_name, parameters=parameters)
        task.save()
        return task


class ExecutionParameters(models.Model):
    minimal_annotations = models.IntegerField()


class Task(models.Model):
    protocol = models.ForeignKey(Protocol, related_name="tasks")
    task_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    parameters = models.ForeignKey(ExecutionParameters)


    def add_item(self, data):
        item = Item(task_id=self.id, data=data)
        item.save()
        return item


    def get_item(self):
        return None


    class Meta:
        ordering = ['-created']
