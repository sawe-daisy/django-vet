from django.shortcuts import render
from urllib import request
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .serializer import VetSerializer, UserSerializer
from .models import Veterinary
from rest_framework.decorators import permission_classes
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
import json
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from itertools import chain
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.
# class 


def welcome(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    # def get(self, request, format=None):
    serializer_class=UserSerializer
    queryset=User.objects.all()
        # serializer=UserSerializer(queryset, many=True)
        # return Response(serializer.data)
    
    # def post(self, request, format=None):
    #     serializer=UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    
    def put(self, request, pk, format=None):
        vet=Veterinary.objects.get(pk=pk)
        serializer=VetSerializer(vet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vet=Veterinary.objects.get(pk=pk)
        Veterinary.delete(vet)
        return Response(status=status.HTTP_204_NO_CONTENT)


