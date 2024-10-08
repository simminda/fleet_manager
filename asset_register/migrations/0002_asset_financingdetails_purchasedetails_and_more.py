# Generated by Django 5.0.2 on 2024-08-15 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('sub_category', models.CharField(max_length=100)),
                ('classification', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('vin', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funding_institution', models.CharField(max_length=100)),
                ('loan_ref_number', models.CharField(max_length=100)),
                ('loan_end_date', models.DateField()),
                ('loan_terms', models.IntegerField()),
                ('installments', models.DecimalField(decimal_places=2, max_digits=15)),
                ('reg_no', models.CharField(max_length=100)),
                ('fleet_no', models.CharField(max_length=100)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset_register.asset')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('dealership', models.CharField(max_length=100)),
                ('invoice_no', models.CharField(max_length=100)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('disc_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('disc_expiry_date', models.DateField()),
                ('asset', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asset_register.asset')),
            ],
        ),
        migrations.DeleteModel(
            name='Vehicle',
        ),
    ]
