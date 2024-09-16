from django.db import models


class Asset(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    vin = models.CharField(max_length=100, unique=True)


class PurchaseDetails(models.Model):
    purchase_date = models.DateField()
    dealership = models.CharField(max_length=100)
    invoice_no = models.CharField(max_length=100)
    cost_price = models.DecimalField(max_digits=15, decimal_places=3)
    disc_fee = models.DecimalField(max_digits=15, decimal_places=3, null=True, blank=True)
    disc_expiry_date = models.DateField()
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)


class FinancingDetails(models.Model):
    funding_institution = models.CharField(max_length=100)
    loan_ref_number = models.CharField(max_length=100)
    loan_end_date = models.DateField()
    loan_terms = models.IntegerField()
    installments = models.DecimalField(max_digits=15, decimal_places=3)
    reg_no = models.CharField(max_length=100)
    fleet_no = models.CharField(max_length=100)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

