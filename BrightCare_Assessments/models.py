# BrightCare_Assessments\models.py
from django.db import models

class RiskFactor(models.Model):
    risk_title = models.CharField(blank=False, null=False, max_length=100)
    description = models.TextField(blank=False, null=False, default='')

    def __str__(self):
        self.risk_title


class RiskAssesment(models.Model):
    young_person = models.ForeignKey('BrightCare_YoungPerson.YoungPerson', on_delete=models.CASCADE, related_name='assessments')
    assessed_by = models.ForeignKey('BrightCare_staff.StaffProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name='assessments')
    risk_factors = models.ManyToManyField(RiskFactor, blank=True, related_name='assessments')
    likelihood_score = models.IntegerField(default=0)
    impact_score = models.IntegerField(default=0)
    overall_sccore = models.CharField(max_length=100, blank=True, null=True, default='')
    notes = models.TextField(blank=True, null=True, max_length=2000, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        date_str = self.created_at.date() if self.created_at else "N/A"
        return f"Assesment for {self.young_person} on {date_str}."
    