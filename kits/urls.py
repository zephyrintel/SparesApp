from django.urls import path
from . import views

urlpatterns = [
    path('kit-selector/', views.kit_selector, name='kit_selector'),
]
