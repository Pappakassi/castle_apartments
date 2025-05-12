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

    def __str__(self):
        return f"Offer for {self.apartment.title} by {self.buyer.username}"
