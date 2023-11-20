from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.EnergyDevice)
admin.site.register(models.Facility)
admin.site.register(models.EnergyAudit)
