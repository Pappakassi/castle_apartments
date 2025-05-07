from django.db import models
from django.contrib.auth.models import User

class Apartments(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, default='Reykjavik')
    postal_code = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    type = models.CharField(max_length=50, default='Apartment')
    listing_price = models.PositiveIntegerField()
    is_sold = models.BooleanField(default=False)
    listing_date = models.DateField(auto_now_add=True)
    image = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.title} ({self.city})"


#byggt á fyrsta data.py sem við gerðum:
# class Apartment(models.Model):
#     title = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     price = models.PositiveIntegerField()
#     is_sold = models.BooleanField(default=False)
#     description = models.TextField()
#     image = models.URLField(max_length=500, blank=True)
#
#     def __str__(self):
#         return f"{self.title} — {self.address}"
