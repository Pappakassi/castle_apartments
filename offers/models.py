from django.db import models
from django.contrib.auth.models import User  # default User model

#Option A – Buyer is just a user (using Django's built-in User)
#Hérna er ekki verið að búa til profile utan um buyer
class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    posted_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.buyer.username}"
