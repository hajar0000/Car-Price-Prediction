# Generated by Django 5.1.4 on 2024-12-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('selling_price', models.FloatField()),
                ('present_price', models.FloatField()),
                ('kms_driven', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('CNG', 'CNG')], max_length=10)),
                ('seller_type', models.CharField(choices=[('Dealer', 'Dealer'), ('Individual', 'Individual')], max_length=10)),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=10)),
                ('owner', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
                'ordering': ['year'],
            },
        ),
    ]