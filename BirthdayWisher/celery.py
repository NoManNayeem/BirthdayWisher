
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from pytz import timezone
from datetime import timedelta


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BirthdayWisher.settings')

app = Celery('BirthdayWisher')

app.conf.enable_utc = False
app.conf.update(timezone='Asia/Dhaka')

app.config_from_object('django.conf:settings', namespace='CELERY')

CELERY_BEAT_SCHEDULE = {
    'send-birthday-wishes': {
        'task': 'customers.tasks.send_birthday_wishes',
        'schedule': timedelta(days=1),  # Daily schedule
        # 'schedule': timedelta(seconds=10),  # To check if the functions trigger properly
    },
}


# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
   