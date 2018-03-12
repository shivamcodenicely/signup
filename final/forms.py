from django import forms
from django.forms import ModelForm
from app_name.models import AllocationPlan

class AllocationPlanForm(ModelForm):
    class Meta:
        model = AllocationPlan
