from rest_framework import generics

from crowdhub.settings.auth import AUTH_AUTHENTICATION_CLASSES, AUTH_PERMISSION_CLASSES


class BaseListView(generics.ListAPIView):
    authentication_classes = AUTH_AUTHENTICATION_CLASSES
    permission_classes = AUTH_PERMISSION_CLASSES
    queryset = []
    serializer_class = None


class BaseCreateListView(generics.CreateAPIView):
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
