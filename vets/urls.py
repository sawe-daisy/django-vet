from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path, include, re_path
from . import views
from .views import VeterinaryViewSet, welcome, VeterinaryUpdateViewSet, UserViewSet

userSignup=UserViewSet.as_view({
    'get':'list',
    'post':'create'
})

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('', welcome),
    path('vets/', VeterinaryViewSet.as_view()),
    path('register/', userSignup, name='register'),
    path('vets/update/<int:pk>/', VeterinaryUpdateViewSet.as_view()),
]