from django.contrib import admin
from django.urls import path, include

app_name = 'BrightCare_base'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('BrightCare_staff.urls')),
    path('care-homes/', include('BrightCare_CareHomes.urls')),
    path('young-person/', include('BrightCare_YoungPerson.urls')),
    path('assessments/', include('BrightCare_Assessments.urls')),
    path('incidents/', include('BrightCare_Incidents.urls')),
]
