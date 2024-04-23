from celery import shared_task
from django.utils import timezone
from .models import Customer
from .utils import simulate_email 


@shared_task
def send_birthday_wishes():
    today = timezone.now().date()
    customers = Customer.objects.filter(birthday=today)
    for customer in customers:
        simulate_email(customer.email, "Happy Birthday!", "We wish you a happy birthday!")
