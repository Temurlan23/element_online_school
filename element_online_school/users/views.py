from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from .models import User
from .filters import UserFilterSet

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filterset_class = UserFilterSet
	
	