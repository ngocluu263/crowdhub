from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^$', views.profile),
    url(r'users/login', views.login),
    url(r'users/logout', views.logout),
    url(r'users/register', views.register),
    url(r'users/profile', views.profile),
]
