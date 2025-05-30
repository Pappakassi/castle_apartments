# Generated by Django 4.0.4 on 2025-05-13 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_purchaseoffer_delete_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('national_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('credit_card', 'Credit Card'), ('bank_transfer', 'Bank Transfer'), ('mortgage', 'Mortgage')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MortgagePayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=255)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offers.payment')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCardPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder_name', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=20)),
                ('expiry_date', models.CharField(max_length=5)),
                ('cvc', models.CharField(max_length=4)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offers.payment')),
            ],
        ),
        migrations.CreateModel(
            name='BankTransferPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=34)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='offers.payment')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseoffer',
            name='contact_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='offers.contactinfo'),
        ),
        migrations.AddField(
            model_name='purchaseoffer',
            name='payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='offers.payment'),
        ),
    ]
