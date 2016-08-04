from mongoengine import Document
from mongoengine.fields import IntField, DictField, ListField

import tasks


class Item(Document):
    task_id = IntField()
    data = DictField()
    annotations = ListField()

    @property
    def task(self):
        return tasks.models.Task.objects.get(id=self.task_id)


class Annotation(Document):
    item_id = IntField()
    user_id = IntField()
    data = DictField()

    @property
    def task(self):
        return tasks.models.Item.objects.get(id=self.item_id)

