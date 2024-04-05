# Generated by Django 5.0.3 on 2024-04-02 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loan", "0004_alter_loan_status"),
        ("user", "0002_rename_is_doctor_user_is_agent_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaymentPosting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField(auto_now_add=True)),
                ("is_payment_made", models.BooleanField()),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[
                            ("Disbursement", "Disbursement,"),
                            ("Loan Repayment", "Loan Repayment"),
                            ("Penalty", "Penalty"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client",
                        to="user.user",
                    ),
                ),
                (
                    "loan_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="loans",
                        to="user.user",
                    ),
                ),
            ],
        ),
    ]
