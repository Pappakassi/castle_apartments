# Generated by Django 4.0.4 on 2025-05-12 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_alter_apartment_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('seller_type', models.CharField(choices=[('individual', 'Individual'), ('agency', 'Real Estate Agency')], max_length=20)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('street_name', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(default='Reykjavik', max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=20)),
                ('logo', models.URLField(blank=True, max_length=500)),
                ('cover_image', models.URLField(blank=True, max_length=500)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='num_bathrooms',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='apartment',
            name='num_bedrooms',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='apartment',
            name='num_rooms',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='apartment',
            name='square_meters',
            field=models.PositiveIntegerField(default=0),
        ),
        # migrations.AlterField(
        #     model_name='apartment',
        #     name='seller',
        #     field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='apartments.seller'),
        # ),
    ]
