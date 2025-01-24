# BrightCare_CareHomes\models.py
from django.db import models


class CareHomes(models.Model):
    care_home_name = models.CharField(
        max_length=255, blank=False, null=False, default=""
    )
    address_line_1 = models.CharField(
        max_length=200, blank=False, null=False, default=""
    )
    address_line_2 = models.CharField(max_length=200, blank=True, null=True, default="")
    city_town = models.CharField(max_length=100, blank=True, null=True, default="")
    county = models.CharField(max_length=100, blank=True, null=True, default="")
    post_code = models.CharField(max_length=20, blank=True, null=True, default="")
    phone_number = models.CharField(max_length=50, blank=True, null=True, default="")
    capacity = models.PositiveIntegerField(blank=False, null=False, default=0)
    registration_number = models.CharField(blank=True, null=True, max_length=100, default="")

    manager = models.OneToOneField(
        "BrightCare_staff.StaffProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="manages_home",
    )
    staff = models.ManyToManyField(
        "BrightCare_staff.StaffProfile", blank=True, related_name="care_homes"
    )

    def __str__(self):
        return self.care_home_name
