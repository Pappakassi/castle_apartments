from django.contrib.auth.models import User
from django.db import models
from apartments.models import Apartment

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    profile_image = models.TextField(max_length=9999, blank=True)
    favorites = models.ManyToManyField(Apartment, related_name='favorited_by', blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
