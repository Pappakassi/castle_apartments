from django.db import models
from django.contrib.auth.models import User
from apartments.models import Apartment

class PurchaseOffer(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('contingent', 'Contingent'),
    ]

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    expiration_date = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    #extra
    contact_info = models.OneToOneField('ContactInfo', null=True, blank=True, on_delete=models.SET_NULL)
    payment = models.OneToOneField('Payment', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Offer for {self.apartment.title} by {self.buyer.username}"

# --- Contact Information ---
class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address}, {self.city}"


# --- Payment Base ---
class Payment(models.Model):
    PAYMENT_TYPES = [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('mortgage', 'Mortgage'),
    ]
    type = models.CharField(max_length=20, choices=PAYMENT_TYPES)

    def __str__(self):
        return f"{self.get_type_display()} Payment"


# --- Credit Card Payment ---
class CreditCardPayment(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=20)
    expiry_date = models.CharField(max_length=5)
    cvc = models.CharField(max_length=4)


# --- Bank Transfer Payment ---
class BankTransferPayment(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=34)  # IBAN, Swift, etc.


# --- Mortgage Payment ---
class MortgagePayment(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
