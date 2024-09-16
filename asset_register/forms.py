# forms.py
from django import forms
from .models import Asset, PurchaseDetails, FinancingDetails


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'  # Or list specific fields you want to include


class PurchaseDetailsForm(forms.ModelForm):
    class Meta:
        model = PurchaseDetails
        fields = '__all__'  # Or list specific fields


class FinancingDetailsForm(forms.ModelForm):
    class Meta:
        model = FinancingDetails
        fields = '__all__'  # Or list specific fields
