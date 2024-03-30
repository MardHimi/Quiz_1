from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    stack = models.CharField(max_length=100)
    team_lead = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
