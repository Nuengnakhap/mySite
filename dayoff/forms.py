"""
    `forms.py`
    Contains classes to create forms
"""

from django import forms
from django.core.exceptions import ValidationError

from dayoff.models import DayOff

import datetime

class DayOffForm(forms.ModelForm):
    class Meta:
        model = DayOff
        exclude = ['approve_status', 'created_by']
        widgets = {
            'reason': forms.Textarea(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'date_start': forms.DateInput(attrs={'class': 'form-control'}),
            'date_end': forms.DateInput(attrs={'class': 'form-control'}),
        }

    error = None

    def clean(self):
        data = super().clean()

        start = data.get('date_start')
        end = data.get('date_end')

        if start > end:
            self.error = 'End date cannot come before start date'
            raise ValidationError('')
        elif start < datetime.datetime.now().date():
            self.error = 'Please do not fill date in past'
            raise ValidationError('')