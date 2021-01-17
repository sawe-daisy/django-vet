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
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

def welcome(request):
    return render(request, 'index.html')

@IsAdminUser
class VeterinaryViewSet(APIView):
    def get(self, request, format=None):
        vets=Veterinary.objects.all()
        serializer=VetSerializer(vets, many=True)
        return Response(serializer.data)
