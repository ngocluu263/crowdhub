from django.conf.urls import url

from tasks.api import TaskList, ItemList, AnnotationList

urlpatterns = [
    url(r'api/users/tasks', TaskList.as_view()),
    url(r'api/users/items', ItemList.as_view()),
    url(r'api/users/annotations', AnnotationList.as_view()),
]
