from .models import Student
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

GENDER_CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ]


class SignUpForm(UserCreationForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    class Meta:
        model=Student
        fields=['first_name','middlename','last_name','dob','gender','mob','Email_address','city','pin','username','password1','password2']
        labels={'Email_address':'Email'}
        help_text={'mob':'10 digits only'}

    def clean(self):
        cleaned_data=super().clean()
        valmob=self.cleaned_data['mob']
        if(len(str(valmob))!=10):
            raise ValidationError("Mobile number should be of 10 digits only")
        return self.cleaned_data


class SearchForm(forms.Form):
    first_name=forms.CharField(label='Firstname',max_length=100)

