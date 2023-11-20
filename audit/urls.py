from django.urls import path
from . import views

urlpatterns = [
    path('create_facility/', views.create_facility, name='create_facility'),
    path('create_energy_device/', views.create_energy_device, name='create_energy_device'),
    path('create_energy_audit/', views.create_energy_audit, name='create_energy_audit'),
    path('get_energy_audits/', views.get_audits, name='get_energy_audit'),
    path('get_energy_devices/', views.get_devices, name='get_energy_devices'),
    path('get_facility_devices/', views.get_facilities_devices, name='get_facility_devices'),
    path('get_facility_audits/', views.get_facilities_audits, name='get_facility_audits'),
    
    path('get_facilities/', views.get_facilities, name='get_facilities'),
]
