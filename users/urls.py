from django.conf.urls import url

from users.views import login, profile

urlpatterns = [
    url(r'users/login', login),
    url(r'users/profile', profile),
]
