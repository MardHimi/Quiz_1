from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse

def employees(request):
    all_employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': all_employees})

def stack(request):
    all_stacks = Employee.objects.values('stack').distinct()
    return render(request, 'stack.html', {'stacks': all_stacks})

def team_leads(request):
    team_leads = Employee.objects.filter(team_lead__isnull=True)
    return render(request, 'team_leads.html', {'team_leads': team_leads})