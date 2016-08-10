from rest_framework.response import Response
from rest_framework import status

from clients.serializers import ClientSerializer
from clients.models import Client

from crowdhub.api import BaseListView, BaseDetailView, BaseCreateListView


#Client
class ClientList(BaseCreateListView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientDetail(BaseDetailView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

