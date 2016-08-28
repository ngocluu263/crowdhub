from rest_framework.response import Response

from django.contrib.auth.models import User
from users.serializers import UserSerializer

from crowdhub.api import BaseListView, BaseDetailView

class UserList(BaseListView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(BaseDetailView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCurrentDetail(BaseDetailView):
    serializer_class = UserSerializer

    def get(self, request):
        return Response(self.serializer_class(request.user).data)


