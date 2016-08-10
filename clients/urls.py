from django.conf.urls import url

from clients import views, api

urlpatterns = [
    url(r'api/clients/$', api.ClientList.as_view()),
    url(r'api/clients/(?P<pk>[0-9]+)$', api.ClientDetail.as_view()),

    url(r'clients/$', views.list),
    url(r'clients/(?P<client_id>[0-9]+)$', views.view),
]
