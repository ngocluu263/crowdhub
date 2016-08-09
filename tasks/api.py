from rest_framework.response import Response
from rest_framework import status

from tasks.serializers import ProtocolSerializer, TaskSerializer, ItemSerializer, AnnotationSerializer
from tasks.models.base import Protocol, Task
from tasks.models.data import Item, Annotation

from crowdhub.api import BaseListView, BaseDetailView, BaseCreateListView

from utils.helpers import is_json
import json


#Protocol
class ProtocolList(BaseCreateListView):
    serializer_class = ProtocolSerializer
    queryset = Protocol.objects.all()


class ProtocolDetail(BaseDetailView):
    serializer_class = ProtocolSerializer
    queryset = Protocol.objects.all()


class ProtocolTasksList(BaseCreateListView):
    serializer_class = TaskSerializer

    def get(self, request, pid, *args, **kwargs):
        tasks = Protocol.objects.get(id=pid).tasks
        return Response(self.serializer_class(tasks, many=True).data)

    def post(self, request, pid, *args, **kwargs):
        if not request.user.has_perm('crowdhub.can_add_task'):
            return Response("This user has no permission to create new task.", status=status.HTTP_403_FORBIDDEN)

        protocol = Protocol.objects.get(id=pid)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            task = Task(**serializer.validated_data)
            created_task = protocol.add_task(task)
            return Response(self.serializer_class(created_task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Tasks
class TaskList(BaseListView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDetail(BaseDetailView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


#Items
class TaskItemsList(BaseCreateListView):
    serializer_class = ItemSerializer

    def get(self, request, tid, *args, **kwargs):
        items = Task.objects.get(id=tid).items
        return Response(self.serializer_class(items, many=True).data)

    def post(self, request, tid, *args, **kwargs):
        task = Task.objects.get(id=tid)

        item_data = request.data['data']
        if is_json(item_data):
            item = Item(data=json.loads(item_data))
            created_item = task.add_item(item)
            return Response(self.serializer_class(created_item).data, status=status.HTTP_201_CREATED)
        return Response("Wrong format of input data.", status=status.HTTP_400_BAD_REQUEST)


class TaskItemsDetail(BaseDetailView):
    serializer_class = ItemSerializer

    def get(self, request, tid, iid, *args, **kwargs):
        item = Task.objects.get(id=tid).items.get(id=iid)
        return Response(self.serializer_class(item).data)


class NextItemDetail(BaseDetailView):
    serializer_class = ItemSerializer

    def get(self, request, tid, *args, **kwargs):
        item = Task.objects.get(id=tid).get_next_item()
        return Response(self.serializer_class(item).data)


#Annotations
class ItemAnnotationList(BaseCreateListView):
    serializer_class = AnnotationSerializer

    def get(self, request, tid, iid, *args, **kwargs):
        item = Task.objects.get(id=tid).items.get(id=iid)
        return Response(self.serializer_class(item.annotations, many=True).data)

    def post(self, request, tid, iid, *args, **kwargs):
        item = Task.objects.get(id=tid).items.get(id=iid)

        annotation_data = request.data['data']
        if is_json(annotation_data):
            annotation = Annotation(data=json.loads(annotation_data))
            created_annotation = item.add_annotation(annotation, request.user.id)
            return Response(self.serializer_class(created_annotation).data, status=status.HTTP_201_CREATED)
        return Response("Wrong format of input data.", status=status.HTTP_400_BAD_REQUEST)


class ItemAnnotationDetail(BaseDetailView):
    serializer_class = AnnotationSerializer

    def get(self, request, tid, iid, aid, *args, **kwargs):
        item = Task.objects.get(id=tid).items.get(id=iid)
        annotation = item.annotations.get(id=aid)
        return Response(self.serializer_class(annotation).data)
