from django.db import models

class Car(models.Model):
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('CNG', 'CNG'), 
    ]
    SELLER_CHOICES = [
        ('Dealer', 'Dealer'),
        ('Individual', 'Individual'),
    ]
    TRANSMISSION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]

    car_name = models.CharField(max_length=100)  # Name of the car
    year = models.PositiveIntegerField()  # Manufacturing year
    selling_price = models.FloatField()  # Selling price 
    present_price = models.FloatField()  # Current price 
    kms_driven = models.PositiveIntegerField()  # Kilometers driven
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES)  # Fuel type
    seller_type = models.CharField(max_length=10, choices=SELLER_CHOICES)  # Seller type
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)  # Transmission type
    owner = models.PositiveSmallIntegerField()  # Number of previous owners

    def __str__(self):
        return f"{self.car_name} ({self.year})"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ['year']  # Default ordering by year
