from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path, include, re_path
from . import views
from .views import VeterinaryViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('', welcome, name='welcome'),
    path('vets/', VeterinaryViewSet.as_view()),
]