from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Veterinary
from django.contrib.auth.models import User
from rest_framework import viewsets

class UserSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_password(password: str) ->str:
        return make_password(password)
    class Meta:
        model= User
        fields='__all__'
        fields=['username','first_name', 'last_name', "email",'is_staff','password']

class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model= Veterinary
        fields= '__all__'