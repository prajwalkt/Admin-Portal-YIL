from django.db import models
from django.conf import settings


class Invoice(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    total = models.FloatField(
        null=True,
        blank=True
    )

    amount = models.FloatField(
        null=True,
        blank=True
    )

    payment_complete = models.BooleanField(
        default=False
    )

    invoice_code = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    customer_name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    region = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    po_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    invoice_pdf = models.FileField(
        upload_to='invoices/',
        blank=True,
        null=True
    )

    po_document = models.FileField(
        upload_to='purchase_orders/',
        blank=True,
        null=True
    )

    payment_proof = models.FileField(
        upload_to='payment_proofs/',
        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.invoice_code or f"Invoice {self.id}"