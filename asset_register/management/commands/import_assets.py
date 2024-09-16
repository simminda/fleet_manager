import csv
import os
from datetime import datetime
from django.core.management.base import BaseCommand
from asset_register.models import Asset, PurchaseDetails, FinancingDetails
from django.core.exceptions import ValidationError

class Command(BaseCommand):
    help = 'Import assets from a CSV file'

    def convert_date_format(self, date_str, input_format='%Y/%m/%d', output_format='%Y-%m-%d'):
        if not date_str:
            # Ignore empty date fields
            return None
        try:
            # Parse the date using the input format
            date_obj = datetime.strptime(date_str, input_format)
            # Convert the date to the desired output format
            return date_obj.strftime(output_format)
        except ValueError:
            # Handle invalid date format
            print(f'Invalid date format for date: {date_str}. Expected format: yyyy/mm/dd')
            return None

    def handle_decimal_field(self, value):
        if not value or value.strip() == '':
            return 0.00  # Default to 0.00 if the field is empty
        try:
            return round(float(value), 3)  # Ensure the value is rounded to 3 decimal places
        except ValueError:
            print(f"Invalid decimal value: {value}. Defaulting to 0.00.")
            return 0.00

    def handle(self, *args, **kwargs):
        # Get the absolute path of the CSV file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(base_dir, 'initial_fleet.csv')

        with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)

            print("Column Names:", reader.fieldnames)

            for row in reader:
                try:
                    # Convert dates
                    purchase_date = self.convert_date_format(row.get('purchase_date'))
                    disc_expiry_date = self.convert_date_format(row.get('disc_expiry_date'))
                    loan_end_date = self.convert_date_format(row.get('loan_end_date'))

                    # Process decimal fields
                    cost_price = self.handle_decimal_field(row.get('cost_price'))
                    disc_fee = self.handle_decimal_field(row.get('disc_fee'))
                    installments = self.handle_decimal_field(row.get('installments'))

                    # Create Asset
                    asset = Asset.objects.create(
                        year=row.get('year'),
                        make=row.get('make'),
                        model=row.get('model'),
                        vehicle_type=row.get('vehicle_type'),
                        sub_category=row.get('sub_category'),
                        classification=row.get('classification'),
                        status=row.get('status'),
                        vin=row.get('vin'),
                    )

                    # Create PurchaseDetails
                    PurchaseDetails.objects.create(
                        purchase_date=purchase_date,
                        dealership=row.get('dealership'),
                        invoice_no=row.get('invoice_no'),
                        cost_price=cost_price,
                        disc_fee=disc_fee,
                        disc_expiry_date=disc_expiry_date,
                        asset=asset
                    )

                    # Create FinancingDetails
                    FinancingDetails.objects.create(
                        funding_institution=row.get('funding_institution'),
                        loan_ref_number=row.get('loan_ref_number'),
                        loan_end_date=loan_end_date,
                        loan_terms=row.get('loan_terms'),
                        installments=installments,
                        reg_no=row.get('reg_no'),
                        fleet_no=row.get('fleet_no'),
                        asset=asset
                    )

                except ValidationError as e:
                    print(f"Validation Error: {e} in row: {row}")
                except (ValueError, TypeError) as e:
                    print(f"Error processing row (invalid data type): {row}. Error: {e}")
                except Exception as e:
                    print(f"Error processing row: {row}. Error: {e}")

        self.stdout.write(self.style.SUCCESS('Successfully imported assets'))
