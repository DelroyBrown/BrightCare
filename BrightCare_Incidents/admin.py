# BrightCare_Incidents\admin.py
from django.contrib import admin
from .models import Incident


admin.site.register(Incident)
