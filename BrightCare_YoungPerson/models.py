# BrightCare_YoungPerson\models.py
from django.db import models


class Guardian(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False, default="")
    last_name = models.CharField(max_length=100, blank=False, null=False, default="")
    relationship = models.CharField(max_length=50, blank=True, null=True, default="")
    email = models.EmailField(max_length=100, blank=True, null=True, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.relationship})"


class YoungPerson(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False, default="")
    last_name = models.CharField(max_length=100, blank=False, null=False, default="")
    date_of_birth = models.DateField(default=0)
    care_home = models.ForeignKey(
        "BrightCare_CareHomes.CareHomes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    guardians = models.ManyToManyField(
        Guardian, blank=True, related_name="young_people"
    )
    medical_info = models.TextField(blank=True, null=True, default="")
    allergies = models.TextField(blank=True, null=True, default="")
    special_educational_needs = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='young_person_portrait', default='')
    admission_date = models.DateField(blank=True, null=True)
    discharge_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.care_home}"
