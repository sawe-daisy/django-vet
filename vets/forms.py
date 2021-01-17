from django import forms
from django.contrib.auth.models import User
from .models import Veterinary
from django.contrib.auth.forms import UserCreationForm

class vetForm(forms.ModelForm):
    class Meta:
        model= Veterinary
        fields='__all__'