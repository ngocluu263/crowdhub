from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer
from rest_framework import serializers

from tasks.models import Task
from tasks.models_data import Item, Annotation


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


class ItemSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Item


class AnnotationSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Annotation


