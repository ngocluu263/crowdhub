from django.conf.urls import url

from users import views
from users import api

urlpatterns = [
    url(r'^$', views.profile),
    url(r'^$', views.profile),
    url(r'users/login', views.login),
    url(r'users/logout', views.logout),
    url(r'users/register', views.register),
    url(r'users/profile', views.profile),

    url(r'api/users/$', api.UserList.as_view()),
    url(r'api/users/current', api.UserCurrentDetail.as_view()),
    url(r'api/users/(?P<pk>[0-9]+)$', api.UserDetail.as_view()),
]
