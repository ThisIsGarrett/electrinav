from django import forms
from .models import TimeEntry

class TimeEntryForm(forms.ModelForm):
    class Meta:
        model = TimeEntry
        fields = ['date', 'project_name', 'hours_worked', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
