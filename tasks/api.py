from tasks.serializers import TaskSerializer, ItemSerializer, AnnotationSerializer
from tasks.models import Task
from tasks.models_data import Item, Annotation

from rest_framework import generics

from crowdhub.settings.auth import AUTH_AUTHENTICATION_CLASSES, AUTH_PERMISSION_CLASSES

class TaskList(generics.ListAPIView):
    authentication_classes = AUTH_AUTHENTICATION_CLASSES
    permission_classes = AUTH_PERMISSION_CLASSES
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ItemList(generics.ListAPIView):
    authentication_classes = AUTH_AUTHENTICATION_CLASSES
    permission_classes = AUTH_PERMISSION_CLASSES
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AnnotationList(generics.CreateAPIView):
    authentication_classes = AUTH_AUTHENTICATION_CLASSES
    permission_classes = AUTH_PERMISSION_CLASSES
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

