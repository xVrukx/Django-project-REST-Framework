#import

from celery import shared_task
from django.core.mail import send_mail

#--------------------------------------------------------------
#tasks
@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'developeryuvrajsirganor@gmail.com',  
        recipient_list,
        fail_silently=False,
    )
    return f"Email sent to {recipient_list}"