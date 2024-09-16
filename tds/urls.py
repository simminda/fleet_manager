from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('asset_register.urls')),
    path('asset_register/', include('asset_register.urls')),
]
