from rest_framework import serializers
from .models import Veterinary
from rest_framework import viewsets

class VetSerializer(serializers.ModelSerializer):
    class Meta:
        model= Veterinary
        fields= '__all__'