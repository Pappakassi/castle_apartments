from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    SELLER_TYPES = [
        ('individual', 'Individual'),
        ('agency', 'Real Estate Agency'),
    ]

    name = models.CharField(max_length=255)
    seller_type = models.CharField(max_length=20, choices=SELLER_TYPES)
    address = models.CharField(max_length=255, blank=True)
    street_name = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, default='Reykjavik')
    postal_code = models.CharField(max_length=20, blank=True)
    logo = models.URLField(max_length=500, blank=True)
    cover_image = models.URLField(max_length=500, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=True)
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

    # Newly added fields:
    num_rooms = models.PositiveIntegerField(default=1)
    num_bedrooms = models.PositiveIntegerField(default=1)
    num_bathrooms = models.PositiveIntegerField(default=1)
    square_meters = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title} ({self.city})"

class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField(max_length=500)
    caption = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta: # default ordering
        ordering = ['image_url']

    def __str__(self):
        return f"Image for {self.apartment.title}"
