from django import forms
from .models import Rent

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RentForm(forms.ModelForm):

    class Meta:
        model = Rent
        fields = ('tipo', 'observacao')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nome = forms.CharField()
    sobrenome = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'nome', 'sobrenome', 'email', 'password1', 'password2']

