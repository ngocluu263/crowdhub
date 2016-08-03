from django.conf.urls import url

from tasks.api import TaskList, ItemList, AnnotationList
from tasks import views

urlpatterns = [
    url(r'api/tasks/tasks', TaskList.as_view()),
    url(r'api/tasks/items', ItemList.as_view()),
    url(r'api/tasks/annotations', AnnotationList.as_view()),

    url(r'tasks/(?P<task_id>[0-9]+)$', views.task_view),
    url(r'tasks', views.tasks_list),
]
