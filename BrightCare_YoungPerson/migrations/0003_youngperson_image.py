# Generated by Django 5.1.5 on 2025-01-24 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BrightCare_YoungPerson', '0002_alter_youngperson_guardians'),
    ]

    operations = [
        migrations.AddField(
            model_name='youngperson',
            name='image',
            field=models.ImageField(default='', upload_to='young_person_portrait'),
        ),
    ]
