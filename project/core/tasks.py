from celery import shared_task
from django.core.management import call_command  # NEW


@shared_task
def sample_task():
    print("==========================")
    print("The sample task just ran.")
    print("--------------------------")


# NEW
@shared_task
def send_email_report():
    call_command(
        "email_report",
    )


# NEW
@shared_task
def update_currency_rates():
    call_command(
        "update_currencies",
    )
