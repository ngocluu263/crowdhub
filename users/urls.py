from django.conf.urls import url

from users.views import login, profile

urlpatterns = [
    url(r'login', login),
    url(r'profile', profile),
]
