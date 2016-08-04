from tasks.serializers import TaskSerializer, ItemSerializer, AnnotationSerializer
from tasks.models import Task
from tasks.models_data import Item, Annotation

from crowdhub.api import BaseListView, BaseCreateListView


class TaskList(BaseListView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ItemList(BaseListView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AnnotationList(BaseCreateListView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer



