from django.shortcuts import render, get_object_or_404, redirect
from .models import Asset, PurchaseDetails, FinancingDetails
from django.db.models import Sum, Count


def home(request):
    # Count and total cost per vehicle type
    vehicle_summary = Asset.objects.values('vehicle_type').annotate(
        total_cost=Sum('purchasedetails__cost_price'),
        count=Count('id')
    ).order_by('vehicle_type')

    # Finance house and count for financed vehicles
    financed_data = FinancingDetails.objects.values('funding_institution').annotate(
        count=Count('id')
    ).order_by('funding_institution')

    context = {
        'financed_data': financed_data,
    }

    return render(request, 'asset_register/home.html', context)


def asset_list(request):
    # Get all assets
    assets = Asset.objects.all()

    # Aggregate data
    vehicle_summary = Asset.objects.values('vehicle_type').annotate(
        count=Count('id'),
        # Aggregate cost_price from PurchaseDetails
        total_cost=Sum('purchasedetails__cost_price')
    ).order_by('vehicle_type')

    return render(request, 'asset_register/home.html', {'assets': assets, 'vehicle_summary': vehicle_summary})


def trucks(request):
    # Filter assets where vehicle_type is "Truck" and status is "active"
    filtered_assets = Asset.objects.filter(
        vehicle_type='Truck', status='Active')
    return render(request, 'asset_register/trucks.html', {'assets': filtered_assets})


def finance_summary(request):
    financed_data = FinancingDetails.objects.values('funding_institution').annotate(
        count=Count('id'),  # Count of assets financed by this institution
        # Sum of installments for this institution
        total_installments=Sum('installments')
    )

    context = {
        'financed_data': financed_data,
    }
    return render(request, 'asset_register/finance.html', context)


def licensing(request):
    return render(request, 'asset_register/licensing.html')


def asset_view(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    purchase_details = PurchaseDetails.objects.get(asset=asset)
    financing_details = FinancingDetails.objects.filter(asset=asset)

    context = {
        'asset': asset,
        'purchase_details': purchase_details,
        'financing_details': financing_details,
    }
    return render(request, 'asset_register/asset_screen.html', context)


def search_view(request):
    query = request.GET.get('q', '')
    if query:
        # Perform search query including VIN
        results = Asset.objects.filter(
            make__icontains=query
        ) | Asset.objects.filter(
            model__icontains=query
        ) | Asset.objects.filter(
            vin__icontains=query
        )
    else:
        results = Asset.objects.none()

    context = {
        'results': results,
        'query': query
    }
    return render(request, 'asset_register/search.html', context)


def edit_asset_view(request, asset_id):
    asset = get_object_or_404(Asset, id=asset_id)

    if request.method == 'POST':
        # Admins can edit the asset
        if request.user.is_superuser:
            asset.year = request.POST.get('year')
            asset.make = request.POST.get('make')
            asset.model = request.POST.get('model')
            asset.vehicle_type = request.POST.get('vehicle_type')
            asset.sub_category = request.POST.get('sub_category')
            asset.classification = request.POST.get('classification')
            asset.status = request.POST.get('status')
            # VIN is not editable and not included here
            asset.save()
            return redirect('asset-detail', asset_id=asset.id)

    context = {'asset': asset}
    return render(request, 'asset_register/asset_screen.html', context)
