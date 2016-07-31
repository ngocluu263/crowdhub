from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

AUTH_AUTHENTICATION_CLASSES = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
AUTH_PERMISSION_CLASSES = (IsAuthenticated,)

LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = "/users/profile/"

