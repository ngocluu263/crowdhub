from django.conf.urls import url

from tasks.api import TaskList, ItemList, AnnotationList

urlpatterns = [
    url(r'api/tasks', TaskList.as_view()),
    url(r'api/items', ItemList.as_view()),
    url(r'api/annotations', AnnotationList.as_view()),
]
