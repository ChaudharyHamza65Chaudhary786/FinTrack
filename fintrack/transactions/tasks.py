from celery import shared_task
from decouple import config
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags

from .models import Transaction
from users.models import User

@shared_task
def send_transaction_emails():         

    users = User.objects.all()

    for user in users:
        user_transactions = Transaction.objects.filter(
            transaction_from_account__holder=user,
            date=timezone.now().date()
        )
        if user_transactions:
            html_message = render_to_string('email.html', {'transactions': user_transactions})
            email = EmailMultiAlternatives(
                "Daily Transaction Report",
                "",
                config('EMAIL_HOST_USER'),
                [user.email]
            )
            email.attach_alternative(html_message, "text/html")
            email.send(fail_silently=False)
