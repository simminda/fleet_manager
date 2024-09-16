from django.urls import path, include
from . import views
from .views import asset_list


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', asset_list, name='asset_list'),
    path('trucks/', views.trucks, name='trucks'),
    path('finance/', views.finance_summary, name='finance_summary'),
    path('license/', views.licensing, name='licensing'),
    path('asset/<int:asset_id>/', views.asset_view, name='asset-detail'),
    path('search/', views.search_view, name='search'),
    path('asset/<int:asset_id>/edit/', views.edit_asset_view, name='edit_asset'),
]
