from rest_framework import serializers
from .models import Course, Topic, Homework, Grade
#from users.serializers import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('id', 'title','start_date')

class TopicSerializer(serializers.ModelSerializer):
	#author = UserSerializer()
	course = CourseSerializer()
	class Meta:
		model = Topic
		fields = ('id','title','duration','author','course')

class HomeworkSerializer(serializers.ModelSerializer):
	topic = TopicSerializer()
	class Meta:
		model = Homework
		fields = ('id','decision','title','complexity','topic')

class GradeSerializer(serializers.ModelSerializer):
	topic = TopicSerializer()
	#student = UserSerializer()
	class Meta:
		model = Grade
		fields = ('id','rating','topic','student')