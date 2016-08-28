from __future__ import unicode_literals

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200)
    package_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    is_embeded = models.BooleanField(default=True)

