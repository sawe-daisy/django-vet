from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import VeterinaryViewSet, VeterinaryUpdateViewSet, UserViewSet, register, postOfficer, PostListView

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

userSignup=UserViewSet.as_view({
    'get':'list',
    'post':'create'
})

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('', PostListView.as_view(), name='welcome'),
    path('register/',register , name='register'),
    path('post/new/', postOfficer, name='post-create'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/logout/', TokenRefreshView.as_view(), name='token_refresh'),
    path('vets/', VeterinaryViewSet.as_view()),
    path('api/register/', userSignup, name='reg'),
    path('vets/update/<int:pk>/', VeterinaryUpdateViewSet.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)