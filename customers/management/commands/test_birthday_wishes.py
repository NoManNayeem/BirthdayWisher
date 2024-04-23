from django.core.management.base import BaseCommand
from customers.tasks import send_birthday_wishes

class Command(BaseCommand):
    help = 'Trigger the birthday wishes task for testing'

    def handle(self, *args, **kwargs):
        send_birthday_wishes.delay()
        self.stdout.write(self.style.SUCCESS('Birthday wishes task triggered.'))
