from django.conf.urls import url

from tasks.api import TaskList, ItemList, AnnotationList

urlpatterns = [
    url(r'api/tasks/tasks', TaskList.as_view()),
    url(r'api/tasks/items', ItemList.as_view()),
    url(r'api/tasks/annotations', AnnotationList.as_view()),
]
