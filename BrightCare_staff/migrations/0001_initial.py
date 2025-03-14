# Generated by Django 5.1.5 on 2025-01-24 15:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BrightCare_CareHomes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=200)),
                ('role', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('department', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('qualifications', models.TextField(blank=True, max_length=2000, null=True)),
                ('dbs_reference', models.CharField(default='', max_length=50)),
                ('dbs_last_checked', models.DateField(blank=True, null=True)),
                ('contact_number', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('care_home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='BrightCare_CareHomes.carehomes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
