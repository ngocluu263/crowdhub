from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^tasks/', include('tasks.urls')),
]

