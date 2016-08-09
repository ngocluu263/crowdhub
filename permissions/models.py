from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class GlobalPermissionManager(models.Manager):
    def get_queryset(self):
        return super(GlobalPermissionManager, self).\
            get_queryset().filter(content_type__model='global_permission')

    def add_or_create(self, *args, **kwargs):
        created = True
        result = GlobalPermission.objects.filter(**kwargs)
        if result:
            created = False
            result = result[0]
        else:
            result = GlobalPermission.objects.create(**kwargs)

        return result, created



class GlobalPermission(Permission):
    """A global permission, not attached to a model"""

    objects = GlobalPermissionManager()

    class Meta:
        proxy = True
        verbose_name = "global_permission"

    def save(self, *args, **kwargs):
        ct, _ = ContentType.objects.get_or_create(
            model=self._meta.verbose_name, app_label=self._meta.app_label,
        )
        self.content_type = ct
        super(GlobalPermission, self).save(*args)


