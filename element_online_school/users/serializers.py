from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('last_name', 'first_name', 'middle_name', 'birth_date', 'phone', 'city', 'is_staff', 'is_superuser', 'course', 'role')