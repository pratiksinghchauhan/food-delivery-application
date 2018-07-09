from django.core.management.base import BaseCommand
from datetime import datetime

def sendConfimation():
    print "hello world"

class Command(BaseCommand):
    def handle(self, **options):
        sendConfimation()