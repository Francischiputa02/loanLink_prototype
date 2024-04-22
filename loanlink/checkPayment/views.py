from django.shortcuts import render
from datetime import datetime
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from loan.models import Loan


# Create your views here.
class Command(BaseCommand):
    help = 'Check for due loan payments and send notifications'

    def handle(self, *args, **options):
        today = datetime.now().date()
        due_loans = Loan.objects.filter(due_date=today)

        for loan in due_loans:
            client_email = loan.client.email
            monthly_repayment = loan.monthly_repayment 
            message = f"Dear customer, your loan payment of ${monthly_repayment} is due today. Please make the payment as soon as possible."

            send_mail(
                'Loan Payment Due Notification',
                message,
                'client_email', 
                [client_email],
                fail_silently=False,
            )

            