from celery import shared_task
from django.core.mail import send_mail

from app.models import User



@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(pk=user_id)
    send_mail(
        'Welcome to our platform!',
        'Hello, {}! We are excited to have you on board.'.format(user.name),
        'ashot.grigoryan8@gmail.com',  # Sender Email
        [user.email],  # Recipient Email
    )
