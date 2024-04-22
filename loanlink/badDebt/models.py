from django.db import models
from loan.models import Loan, LoanTransaction

class BadDebt(models.Model):
    loan_transaction_id = models.ForeignKey(LoanTransaction, verbose_name=_("Loan Transactions"), on_delete=models.CASCADE)
    loan_amount = models.FloatField()
    debt_amount = models.FloatField()
    settlement_date = models.DateTimeField(auto_now_add)


