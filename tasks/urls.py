from django.conf.urls import url

from tasks import api
from tasks import views

urlpatterns = [
    url(r'api/protocols/$', api.ProtocolList.as_view()),
    url(r'api/protocols/(?P<pk>[0-9]+)$', api.ProtocolDetail.as_view()),
    url(r'api/protocols/(?P<pid>[0-9]+)/tasks$', api.ProtocolTasksList.as_view()),

    url(r'api/tasks/$', api.TaskList.as_view()),
    url(r'api/tasks/(?P<pk>[0-9]+)$', api.TaskDetail.as_view()),

    url(r'api/tasks/(?P<tid>[0-9]+)/stats$', api.TaskStatsDetail.as_view()),
    url(r'api/tasks/(?P<tid>[0-9]+)/items$', api.TaskItemsList.as_view()),
    url(r'api/tasks/(?P<tid>[0-9]+)/items/next', api.NextItemDetail.as_view()),
    url(r'api/tasks/(?P<tid>[0-9]+)/items/(?P<iid>[0-9a-z]+)$', api.TaskItemsDetail.as_view()),
    url(r'api/tasks/(?P<tid>[0-9]+)/items/(?P<iid>[0-9a-z]+)/stats$', api.TaskItemsDetailStats.as_view()),

    url(r'api/tasks/(?P<tid>[0-9]+)/items/(?P<iid>[0-9a-z]+)/annotations$', api.ItemAnnotationList.as_view()),
    url(r'api/tasks/(?P<tid>[0-9]+)/items/(?P<iid>[0-9a-z]+)/annotations/(?P<aid>[0-9a-z]+)$', api.ItemAnnotationDetail.as_view()),

    url(r'tasks/$', views.tasks_list),
    url(r'tasks/(?P<task_id>[0-9]+)$', views.task_view),
]
