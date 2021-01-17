from django.shortcuts import render
from urllib import request
from rest_framework.response import Response
from rest_framework import generics
from .serializer import VetSerializer
from .models import Veterinary
from rest_framework.decorators import permission_classes
from django.http import Http404
from rest_framework.views import APIView
import json
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

def welcome(request):
    return render(request, 'index.html')


class VeterinaryViewSet(APIView):
    # permission_classes=[IsAdminUser]
    def get(self, request, format=None):
        vets=Veterinary.objects.all()
        serializer=VetSerializer(vets, many=True)
        return Response(serializer.data)

class VeterinaryUpdateViewSet(APIView):
    # permission_classes=[IsAdminUser]
    def get_object(pk):
        try:
            return Veterinary.objects.get(pk=pk)
        except Veterinary.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        vet=Veterinary.objects.get(pk=pk)
        serializer=VetSerializer(vet)
        return Response(serializer.data)
