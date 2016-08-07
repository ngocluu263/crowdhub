from __future__ import unicode_literals

from mongoengine.context_managers import switch_collection

from django.db import models
from tasks.models.data import Item


class Protocol(models.Model):

    def add_task(self, task):
        task.protocol = self

        if not task.parameters:
            parameters = ExecutionParameters()
            parameters.save()
        task.parameters = parameters
        task.save()

        if not task.items_collection_name:
            task.items_collection_name = "items_{0}".format(task.id)
        task.save()

        return task


class ExecutionParameters(models.Model):
    minimal_annotations = models.IntegerField(default=1)


class Task(models.Model):
    protocol = models.ForeignKey(Protocol, related_name="tasks")
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    parameters = models.ForeignKey(ExecutionParameters, blank=True, null=True)
    items_collection_name = models.CharField(max_length=50, blank=True, null=True)


    def add_item(self, item):
        item.task_id = self.id
        item.switch_collection(self.items_collection_name)
        item.save()
        return item


    @property
    def items(self):
        with switch_collection(Item, self.items_collection_name) as TaskItem:
            return TaskItem.objects.filter(task_id=self.id)


    def get_next_item(self):
        items = self.items
        return items[0]


    class Meta:
        ordering = ['-created']

