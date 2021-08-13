import os
from django.core.management.base import BaseCommand
from spplitAccount.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin',
                                          'shc3851@likelion.org',
                                          'lifeisegg@00')