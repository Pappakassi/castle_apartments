from django.contrib import admin
from .models import (
    PurchaseOffer, ContactInfo, Payment,
    CreditCardPayment, BankTransferPayment, MortgagePayment
)

admin.site.register(PurchaseOffer)
admin.site.register(ContactInfo)
admin.site.register(Payment)
admin.site.register(CreditCardPayment)
admin.site.register(BankTransferPayment)
admin.site.register(MortgagePayment)
