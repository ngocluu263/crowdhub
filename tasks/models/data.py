from mongoengine.context_managers import switch_collection

from mongoengine import Document
from mongoengine.fields import IntField, DictField, ListField, StringField, ReferenceField

import tasks


ANNOTATIONS_COLLECTION = "{0}_annotations"


class Annotation(Document):
    item = ReferenceField('Item')
    user_id = IntField()
    data = DictField()


class Item(Document):
    task_id = IntField()
    data = DictField()

    @property
    def task(self):
        if self.task_id:
            return tasks.models.base.Task.objects.get(id=self.task_id)
        return None


    def add_annotation(self, annotation, user_id):
        annotation.item = self
        annotation.user_id = user_id

        collection_name = ANNOTATIONS_COLLECTION.format(self.task.items_collection_name)
        annotation.switch_collection(collection_name)
        annotation.save()
        return  annotation


    @property
    def annotations(self):
        collection_name = ANNOTATIONS_COLLECTION.format(self.task.items_collection_name)
        with switch_collection(Annotation, collection_name) as ItemAnnotation:
            return ItemAnnotation.objects.filter(item=self)

