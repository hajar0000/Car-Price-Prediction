import csv
from django.core.management.base import BaseCommand
from predict.models import Car

class Command(BaseCommand):
    help = 'Import car data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The file path of the CSV to import')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                Car.objects.create(
                    car_name=row['Car_Name'],
                    year=int(row['Year']),
                    selling_price=float(row['Selling_Price']),
                    present_price=float(row['Present_Price']),
                    kms_driven=int(row['Kms_Driven']),
                    fuel_type=row['Fuel_Type'],
                    seller_type=row['Seller_Type'],
                    transmission=row['Transmission'],
                    owner=int(row['Owner']),
                )
            self.stdout.write(self.style.SUCCESS(f"Successfully imported data from {file_path}"))
