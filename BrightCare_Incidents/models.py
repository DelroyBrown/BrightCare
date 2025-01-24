from django.db import models


class Incident(models.Model):
    young_person = models.ForeignKey(
        "BrightCare_YoungPerson.YoungPerson",
        on_delete=models.CASCADE,
        related_name="incidents",
    )
    reported_by = models.ForeignKey(
        "BrightCare_staff.StaffProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reported_incidents",
    )
    care_home = models.ForeignKey(
        "BrightCare_CareHomes.CareHomes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="incidents",
    )
    location_of_incident = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        help_text="Where did the incident take place",
    )
    incident_title = models.CharField(
        max_length=100, blank=False, null=False, default=""
    )
    description = models.TextField(
        max_length=5000,
        blank=False,
        null=False,
        help_text="Please explain what happened.",
    )
    date_occurred = models.DateTimeField()
    date_reported = models.DateTimeField()

    def __str__(self):
        date_str = self.date_occurred.date() if self.date_occurred else "N/A"
        return f"{self.incident_title} - {self.young_person} on {date_str}"
