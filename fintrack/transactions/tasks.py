from celery import shared_task
from decouple import config
from django.core import mail
from django.utils import timezone

from .models import Transaction
from users.models import User

@shared_task
def send_transaction_emails():         

    users = User.objects.all()

    messages = []

    for user in users:
        user_transactions = Transaction.objects.filter(
            transaction_from_account__holder=user,
            date=timezone.now().date()
        )
        if user_transactions:
            transaction_list = "\n".join(
                [
                    f" Category : {transaction.category},"
                    f" Amount : {transaction.amount}, "
                    f" Description : {transaction.description},"
                    f" Account {transaction.transaction_from_account}" for transaction in user_transactions
                ]
            )
            message = (
                "Daily Transaction Report",
                transaction_list,
                config('EMAIL_HOST_USER'),
                [user.email]
            )
            messages.append(message)

    mail.send_mass_mail(messages, fail_silently=False)
