from celery import shared_task
from decouple import config
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


from users.models import User

@shared_task
def send_password_reset_email(email, url):         
    html_message = render_to_string('reset_password_email.html', {'reset_link': url})
    email = EmailMultiAlternatives(
        "Reset Password Link",
        "",
        config('EMAIL_HOST_USER'),
        [email]
    )
    email.attach_alternative(html_message, "text/html")
    email.send(fail_silently=False)
