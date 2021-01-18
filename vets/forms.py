from django import forms
from django.contrib.auth.models import User
from .models import Veterinary
from django.contrib.auth.forms import UserCreationForm

class vetForm(forms.ModelForm):
    class Meta:
        model= Veterinary
        fields='__all__'

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', "email",'is_staff']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user