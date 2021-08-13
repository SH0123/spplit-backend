import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username='sanghyo').exists():
            User.objects.create_superuser('sanghyo',
                                          'shc3851@likelion.org',
                                          'lifeisegg@00')