from celery import shared_task

from core import settings
from .models import Profile
from django.core.mail import send_mail


@shared_task
def adding_task(x, y):
    return x + y


@shared_task
def send_beat_email():
    for user in Profile.objects.all():
        send_mail(
            'Hello my friend!!!',
            "Check if something new appeared in our website!!! Have a good day!!!",
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    return 'SENT!!!'
