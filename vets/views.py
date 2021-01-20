from django.shortcuts import render
from urllib import request
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, viewsets
from .serializer import VetSerializer, UserSerializer
from django.template import loader 
from .models import Veterinary
from rest_framework.decorators import permission_classes
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .forms import RegistrationForm, vetForm
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


# def welcome(request):
#     return render(request, 'index.html')

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
    permission_classes=[IsAuthenticated]
    def get(self, request, format=None):
        vets=Veterinary.objects.all()
        serializer=VetSerializer(vets, many=True)
        return Response(serializer.data)

class VeterinaryUpdateViewSet(APIView):
    permission_classes=[IsAuthenticated]
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

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
    context={
        'form':form,
    }
    # return loader.render_to_string(request, 'register.html', 'index.html', context)
    return render(request, 'register.html', context)


def postOfficer(request):
    if request.method=="POST":
        form= vetForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            form.save()
            messages.success(request, f'Successfully added {name}')
        return redirect('welcome')
    else:
        form= vetForm()
    context={
        'form':form,
    }
    return render(request, 'posts/vetform.html', context)

class PostListView(ListView):
    model = Veterinary
    template_name = 'index.html'
    context_object_name = 'posts'


class updateOfficerView(UpdateView):
    model= Veterinary
    template_name='posts/vetformupdate.html'
    fields='__all__'

class DeleteOfficerView(DeleteView):
    model= Veterinary
    template_name='posts/vetdeactivate.html'
    success_url=reverse_lazy('welcome')