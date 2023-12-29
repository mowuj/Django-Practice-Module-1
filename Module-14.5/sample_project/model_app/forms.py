from django import forms
from django.forms.widgets import NumberInput
import datetime
from . models import PracticeModel

class PracticeModelForm(forms.ModelForm):
    class Meta:
        model=PracticeModel
        fields = '__all__'