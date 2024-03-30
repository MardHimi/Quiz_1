from django.urls import path
from .views import employees, stack, team_leads

urlpatterns = [
    path('employees/', employees, name='employees'),
    path('stack/', stack, name='stack'),
    path('team-leads/', team_leads, name='team_leads'),
]

