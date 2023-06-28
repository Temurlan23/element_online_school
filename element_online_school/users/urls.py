from django.urls import path
from .views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
path('token/', obtain_auth_token),
]+router.urls