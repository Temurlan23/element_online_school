from rest_framework import serializers
from .models import User
from course.serializers import CourseSerializer

class UserSerializer(serializers.ModelSerializer):
	course = CourseSerializer()

	class Meta:
		model = User
		fields = ('id', 'last_name', 'first_name', 'middle_name', 'birth_date', 'phone', 'city', 'is_staff', 'is_superuser', 'course', 'role')