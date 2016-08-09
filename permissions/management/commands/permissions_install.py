from django.core.management.base import BaseCommand, CommandError
from permissions.models import GlobalPermission
from permissions.config import PERMISSIONS

class Command(BaseCommand):
    help = 'Configure all basic Global Permissions'

    def handle(self, *args, **options):
        for perm in PERMISSIONS:
            permission, created = GlobalPermission.objects.add_or_create(codename=perm[0], name=perm[1])
            message = "reused"
            if created:
                message = "created"
            print "[LOG]: permission: {0} ({1}) was {2}.".format(permission.codename, permission.name, message)

