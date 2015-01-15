from django import forms
#from django.forms.formsets import formset_factory
from django.forms import ModelForm
from models import RegisterUser, Hotel
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email')
        widgets = {
            'password': forms.PasswordInput(),
        }


class RegisterUserForm(ModelForm):
    class Meta:
        model = RegisterUser
        fields = ('country',)


class CityForm(ModelForm):
    class Meta:
        model = Hotel
        fields = ('city',)


class HotelNameForm(ModelForm):
    CHOICES = (("", "----------      "),)
    hotel_names = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = Hotel
        fields = ('hotel_names',)

