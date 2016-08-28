from rest_framework import generics

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from rest_framework.views import APIView

from crowdhub.settings.auth import AUTH_AUTHENTICATION_CLASSES, AUTH_PERMISSION_CLASSES


class BaseView(APIView):
    authentication_classes = AUTH_AUTHENTICATION_CLASSES
    permission_classes = AUTH_PERMISSION_CLASSES
    renderer_classes = (JSONRenderer, )


class BaseListView(generics.ListAPIView):
    authentication_classes = AUTH_AUTHENTICATION_CLASSES
    permission_classes = AUTH_PERMISSION_CLASSES
    queryset = []
    serializer_class = None


class BaseCreateListView(generics.ListCreateAPIView):
    authentication_classes = AUTH_AUTHENTICATION_CLASSES
    permission_classes = AUTH_PERMISSION_CLASSES
    queryset = []
    serializer_class = None


class BaseDetailView(generics.RetrieveAPIView):
    authentication_classes = AUTH_AUTHENTICATION_CLASSES
    permission_classes = AUTH_PERMISSION_CLASSES
    queryset = []
    serializer_class = None


class BaseCreateDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = AUTH_AUTHENTICATION_CLASSES
    permission_classes = AUTH_PERMISSION_CLASSES
    queryset = []
    serializer_class = None


def filter_get(qs, get_params):
    for key, value in get_params.items():
        qs = qs.filter(**{key:value})
    return qs

