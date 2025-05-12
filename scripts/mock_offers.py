import os
import sys
import django
import random
from datetime import timedelta, date

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CastleApartments.settings')
django.setup()

# Now you can safely import your models
from offers.models import PurchaseOffer
from apartments.models import Apartment
from django.contrib.auth.models import User

statuses = ['pending', 'accepted', 'rejected', 'contingent']
users = list(User.objects.all())
apartments = list(Apartment.objects.all())

if not users or not apartments:
    print("Please make sure there are users and apartments in the database.")
else:
    for _ in range(10):
        offer = PurchaseOffer.objects.create(
            apartment=random.choice(apartments),
            buyer=random.choice(users),
            price=random.randint(10_000_000, 150_000_000),
            expiration_date=date.today() + timedelta(days=random.randint(7, 30)),
            status=random.choice(statuses)
        )
        print(f"Created: {offer}")
