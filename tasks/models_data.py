from mongoengine import Document
from mongoengine.fields import IntField, DictField

from tasks.models import Task


class Item(Document):
    task_id = IntField()
    data = DictField()

    @property
    def task(self):
        return Task.objects.get(id=self.task_id)


class Annotation(Document):
    item_id = IntField()
    user_id = IntField()
    data = DictField()

    @property
    def task(self):
        return Item.objects.get(id=self.item_id)

