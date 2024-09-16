from django.contrib import admin
from .models import Asset, PurchaseDetails, FinancingDetails


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('year', 'make', 'model', 'vehicle_type', 'sub_category', 'classification', 'status', 'vin')
    search_fields = ('make', 'model', 'vin')
    list_filter = ('year', 'make', 'status')

@admin.register(PurchaseDetails)
class PurchaseDetailsAdmin(admin.ModelAdmin):
    list_display = ('purchase_date', 'dealership', 'invoice_no', 'cost_price', 'disc_fee', 'disc_expiry_date', 'asset')
    search_fields = ('dealership', 'invoice_no', 'asset__vin')
    list_filter = ('purchase_date', 'dealership')

@admin.register(FinancingDetails)
class FinancingDetailsAdmin(admin.ModelAdmin):
    list_display = ('funding_institution', 'loan_ref_number', 'loan_end_date', 'loan_terms', 'installments', 'reg_no', 'fleet_no', 'asset')
    search_fields = ('funding_institution', 'loan_ref_number', 'asset__vin')
    list_filter = ('loan_end_date', 'funding_institution')
