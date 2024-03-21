from django import forms
import datetime

from django.forms import DateInput


class PlanDate(forms.Form):
    day = forms.DateField(label=('Выберите интересующую Вас дату:'), initial=datetime.date.today,
                          widget=DateInput(attrs={'type': 'date'}))
