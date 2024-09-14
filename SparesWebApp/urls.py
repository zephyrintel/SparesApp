from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kit-selector/', include('kits.urls')),
    path('', lambda request: redirect('kit_selector')),  # Redirect root URL to kit-selector
]
