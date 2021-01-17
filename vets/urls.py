from django.urls import path, include
from .views import *

urlpatterns=[
    path('', welcome, name='welcome')
]