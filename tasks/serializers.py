from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer
from rest_framework import serializers

from tasks.models.base import Protocol, Task
from tasks.models.data import Item, Annotation

class ProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocol
        fields = ('id', 'tasks')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'items_collection_name', 'parameters')


class ItemSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Item
        fields = ('id', 'data')


class AnnotationSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Annotation
        fields = ('id', 'data', 'user_id')
        read_only_fields = ('user_id',)


