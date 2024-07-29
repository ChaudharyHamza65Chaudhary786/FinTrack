from celery import shared_task
from decouple import config
from django.core import mail
from django.utils import timezone

from .models import Transaction


@shared_task
def send_transaction_emails():         
    transactions = Transaction.objects.filter(
        date=timezone.now().date()
    )
    user_emails = transactions.values_list(
        'transaction_from_account__holder__email',
        flat=True
    ).distinct()

    messages = []

    for user_email in user_emails:
        user_transactions = transactions.filter(
            transaction_from_account__holder__email=user_email
        )
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
            [user_email]
        )
        messages.append(message)
    
    mail.send_mass_mail(messages, fail_silently= False)
