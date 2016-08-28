from rest_framework.response import Response
from rest_framework import status

from tasks.serializers import ProtocolSerializer, TaskSerializer, ItemSerializer, AnnotationSerializer
from tasks.models.base import Protocol, Task
from tasks.models.data import Item, Annotation

from crowdhub.api import BaseView, BaseListView, BaseDetailView, BaseCreateListView
from crowdhub.api import filter_get

from utils.helpers import is_json, load_json


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


class TaskStatsDetail(BaseView):
    def get(self, request, tid):
        items_count = Task.objects.get(id=tid).items.count()
        content = {'items_count': items_count}
        return Response(content)



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
            item = Item(data=load_json(item_data))
            created_item = task.add_item(item)
            return Response(self.serializer_class(created_item).data, status=status.HTTP_201_CREATED)
        return Response("Wrong format of input data.", status=status.HTTP_400_BAD_REQUEST)


class TaskItemsDetail(BaseDetailView):
    serializer_class = ItemSerializer

    def get(self, request, tid, iid, *args, **kwargs):
        item = Task.objects.get(id=tid).items.get(id=iid)
        return Response(self.serializer_class(item).data)


class TaskItemsDetailStats(BaseView):
    def get(self, request, tid, iid):
        item = Task.objects.get(id=tid).items.get(id=iid)
        annotations_count = item.annotations.count()
        content = {'annotations_count': annotations_count}
        return Response(content)


class NextItemDetail(BaseDetailView):
    serializer_class = ItemSerializer

    def get(self, request, tid, *args, **kwargs):
        item = Task.objects.get(id=tid).get_next_item()
        return Response(self.serializer_class(item).data)


class ItemAnnotationList(BaseCreateListView):
    serializer_class = AnnotationSerializer
    queryset = Annotation.objects.all()

    def get(self, request, tid, iid, *args, **kwargs):
        item = Task.objects.get(id=tid).items.get(id=iid)
        qs = item.annotations
        qs = filter_get(qs, request.GET)
        return Response(self.serializer_class(qs, many=True).data)

    def post(self, request, tid, iid, *args, **kwargs):
        item = Task.objects.get(id=tid).items.get(id=iid)

        values = {}
        if "data" in request.data:
            values['data'] = load_json(request.data['data'])
        if "id" in request.data:
            values['id'] = request.data['id']
        annotation = Annotation(**values)

        result_annotation, created = item.add_annotation(annotation, request.user.id)
        if result_annotation:
            if created:
                return Response(self.serializer_class(result_annotation).data, status=status.HTTP_201_CREATED)
            else:
                return Response(self.serializer_class(result_annotation).data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response("Requested object does not exist.", status=status.HTTP_400_BAD_REQUEST)


class ItemAnnotationDetail(BaseDetailView):
    serializer_class = AnnotationSerializer

    def get(self, request, tid, iid, aid, *args, **kwargs):
        item = Task.objects.get(id=tid).items.get(id=iid)
        annotation = item.annotations.get(id=aid)
        return Response(self.serializer_class(annotation).data)


#obsluzyc set
#uzyc tego w angularze
#zrobic podsumowanie na stronie z grami
#przeniesc na serwer
#zrobic klienta w unity

