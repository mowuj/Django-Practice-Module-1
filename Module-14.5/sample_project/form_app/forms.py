from django import forms
from django.forms.widgets import NumberInput
import datetime


class PracticeForm(forms.Form):
    name=forms.CharField(label="Please enter your name")
    roll=forms.IntegerField(help_text="enter your Roll")
    password=forms.CharField(widget=forms.PasswordInput())
    comment2=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'row':3}))
    email=forms.EmailField(initial='Your Email')
    agree=forms.BooleanField(initial=True)
    birth_day=forms.DateField(initial=datetime.date.today,widget=NumberInput(attrs={'type':'date'}))
    BIRTH_YEAR_CHOICES=['1995','1996','1997']
    birth_year=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    balance=forms.DecimalField()
    COLORS_CHOICES=[
        ('blue','BLUE'),
        ('red','Red'),
        ('green','Green'),
        ('black','Black'),
    ]
    color=forms.ChoiceField(widget=forms.RadioSelect,choices=COLORS_CHOICES)
    colors=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=COLORS_CHOICES)

