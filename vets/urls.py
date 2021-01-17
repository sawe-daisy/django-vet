from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path, include, re_path
from . import views
from .views import VeterinaryViewSet, welcome, VeterinaryUpdateViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('', welcome),
    path('vets/', VeterinaryViewSet.as_view()),
    path('vets/update/<int:pk>/', VeterinaryUpdateViewSet.as_view()),
]