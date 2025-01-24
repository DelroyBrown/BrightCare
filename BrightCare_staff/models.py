# BrightCare_staff\models.py
from django.db import models
from django.contrib.auth.models import User


class StaffProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=False, null=False, default="")
    role = models.CharField(max_length=100, blank=True, null=True, default="")
    department = models.CharField(max_length=100, blank=True, null=True, default="")
    qualifications = models.TextField(max_length=2000, blank=True, null=True)
    dbs_reference = models.CharField(max_length=50, blank=False, null=False, default="")
    dbs_last_checked = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=100, blank=True, null=True, default="")
    care_home = models.ForeignKey(
        'BrightCare_CareHomes.CareHomes', on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.full_name
