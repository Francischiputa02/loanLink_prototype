# Generated by Django 5.0.3 on 2024-03-28 05:21

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_rename_is_doctor_user_is_agent_and_more'),
        ('userProfile', '0005_agentprofile_bank_agentprofile_bank_acc'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_score', models.BigIntegerField()),
                ('crb', models.BigIntegerField()),
                ('number_of_loan', models.BigIntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.clientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loan_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('period', models.IntegerField()),
                ('purpose', models.CharField(max_length=100)),
                ('balance', models.FloatField()),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(auto_now_add=True)),
                ('method_of_payment', models.CharField(choices=[('mobile', 'mobile'), ('bank account', 'Bank Account'), ('credit card', 'Credit Card'), ('debit card', 'Debit Card'), ('loan', 'Loan')], max_length=200)),
                ('loan_type', models.CharField(choices=[('civil servant loans', 'Civil Servant Loans'), ('famers loans', 'Famers Loans'), ('micro business loans', 'Micro Business Loans')], max_length=200)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=100)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.clientprofile')),
            ],
        ),
        migrations.CreateModel(
            name='LoanTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_payment_made', models.BooleanField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Acctive'), ('closed', 'Closed')], max_length=100)),
                ('transaction_type', models.CharField(choices=[('Disbursement', 'Disbursement,'), ('Loan Repayment', 'Loan Repayment'), ('Penalty', 'Penalty')], max_length=255)),
                ('approved_at', models.DateTimeField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.loan')),
            ],
        ),
    ]
