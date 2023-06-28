from django.shortcuts import render
from rest_framework.generics import (get_object_or_404, GenericAPIView, 
    ListCreateAPIView, RetrieveUpdateDestroyAPIView)
from .serializers import CourseSerializer, TopicSerializer, HomeworkSerializer, GradeSerializer
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from rest_framework import viewsets
from .filters import CourseFilterSet, TopicFilterSet, HomeworkFilterSet
from .models import *
from users.models import *

def course(request):
	courses = Course.objects.all()
	return render(request, "main.html", {"courses": courses})

def topic(request):
	topics = Topic.objects.all()
	return render(request,"main_topic.html", {"topics": topics})

def homework(request):
	homeworks = Homework.objects.all()
	return render(request,"main_homework.html", {"homeworks": homeworks})

def grade(request):
	grades = Grade.objects.all()
	return render(request,"main_grade.html", {"grades": grades})


def about(request):
	return render(request, "about.html",)

#menu = ["О курсе", "Темы", "Домашнее задания", "Успеваемость студента"]

#def main(request):
    #course = Course.objects.all()
    #return render(request, "main.html", {"course": course,"title":'Главная страница'})

def create(request):
	if request.method == "POST":
		course = Course()
		course.title = request.POST.get("title")
		course.start_date = request.POST.get("start_date")
		course.save()
		return HttpResponseRedirect("/")
		# передаем данные в шаблон
	course = Course.objects.all()
	return render(request, "create.html", {"course": course})

def edit(request, id):
    try:
        course = Course.objects.get(id=id)
        if request.method == "POST":
            course.title = request.POST.get("title")
            course.start_date = request.POST.get("start_date")
            course.save()
            return HttpResponseRedirect("/")
        else:
       		return render(request, "edit.html", {"course": course})
    except Course.DoesNotExist:
        return HttpResponseNotFound("<h2>Course not found</h2>")

def delete(request, id):
    try:
        course = Course.objects.get(id=id)
        course.delete()
        return HttpResponseRedirect("/")
    	
    except Course.DoesNotExist:
        return HttpResponseNotFound("<h2>Course not found</h2>")

def create_topic(request):
	if request.method == "POST":
		author = User.objects.filter(id=request.POST.get("author")).first()
		course = Course.objects.filter(id=request.POST.get("course")).first()
		topic = Topic()
		topic.title = request.POST.get("title")
		topic.duration = request.POST.get("duration")
		topic.author = author
		topic.course = course
		topic.save()
		return HttpResponseRedirect("/topic")
		# передаем данные в шаблон

	courses = Course.objects.all()
	users = User.objects.all()
	topic = Topic.objects.all()
	return render(request, "create_topic.html", {"topic": topic, "courses": courses, "users": users})

def edit_topic(request, id):
    try:
        topic = Topic.objects.get(id=id)
        courses = Course.objects.all()
        users = User.objects.all()
        if request.method == "POST":
        	author = User.objects.filter(id=request.POST.get("author")).first()
        	course = Course.objects.filter(id=request.POST.get("course")).first()
        	topic.title = request.POST.get("title")
        	topic.duration = request.POST.get("duration")
        	topic.author = author
        	topic.course = course
        	topic.save()
        	return HttpResponseRedirect("/topic")
        else:
       		return render(request, "edit_topic.html", {"topic": topic, "users": users, "courses": courses})
    except Topic.DoesNotExist:
        return HttpResponseNotFound("<h2>Topic not found</h2>")

def delete_topic(request, id):
    try:
        topic = Topic.objects.get(id=id)
        topic.delete()
        return HttpResponseRedirect("/topic")
    	
    except Topic.DoesNotExist:
        return HttpResponseNotFound("<h2>Topic not found</h2>")


def create_homework(request):
	if request.method == "POST":
		topic = Topic.objects.filter(id=request.POST.get("topic")).first()
		homework = Homework()
		homework.decision = request.POST.get("decision")
		homework.title = request.POST.get("title")
		homework.complexity = request.POST.get("complexity")
		homework.topic = topic
		homework.save()
		return HttpResponseRedirect("/homework")
		# передаем данные в шаблон

	homework = Homework.objects.all()
	topics = Topic.objects.all() 
	return render(request, "create_homework.html", {"homework": homework, "topics": topics})

def edit_homework(request, id):
    try:
        homework = Homework.objects.get(id=id)
        topics = Topic.objects.all()
        if request.method == "POST":
        	topic = Topic.objects.filter(id=request.POST.get("topic")).first()
        	homework.decision = request.POST.get("decision")
        	homework.title = request.POST.get("title")
        	homework.complexity = request.POST.get("complexity")
        	homework.topic = topic
        	homework.save()
        	return HttpResponseRedirect("/homework")
        else:
       		return render(request, "edit_homework.html", {"homework": homework, "topics": topics})
    except Homework.DoesNotExist:
        return HttpResponseNotFound("<h2>Homework not found</h2>")

def delete_homework(request, id):
    try:
        homework = Homework.objects.get(id=id)
        homework.delete()
        return HttpResponseRedirect("/homework")

    except Homework.DoesNotExist:
    	return HttpResponseNotFound("<h2>Homework not found</h2>")


def create_grade(request):
	if request.method == "POST":
		topic = Topic.objects.filter(id=request.POST.get("topic")).first()
		student = User.objects.filter(id=request.POST.get("student")).first()
		
		grade = Grade()
		grade.rating = request.POST.get("rating")
		grade.topic = topic
		grade.student = student
		grade.save()
		return HttpResponseRedirect("/grade")
		# передаем данные в шаблон
	topics = Topic.objects.all()
	users = User.objects.filter(role="STUDENT")
	
	return render(request, "create_grade.html", {"topics": topics, "users": users})

def edit_grade(request, id):
    try:
        grade = Grade.objects.get(id=id)
        if request.method == "POST":
	        topic = Topic.objects.filter(id=request.POST.get("topic")).first()
	        student = User.objects.filter(id=request.POST.get("student")).first()
        	grade.rating = request.POST.get("rating")
        	grade.topic = topic
        	grade.student = student
        	grade.save()
        	return HttpResponseRedirect("/grade")
        else:	
        	topics = Topic.objects.all()
        	users = User.objects.filter(role="STUDENT")
       		return render(request, "edit_grade.html", {"grade": grade, "topics": topics, "users": users})
    except Grade.DoesNotExist:
        return HttpResponseNotFound("<h2>Grade not found</h2>")

def delete_grade(request, id):
    try:
        grade = Grade.objects.get(id=id)
        grade.delete()
        return HttpResponseRedirect("/grade")
    	
    except Grade.DoesNotExist:
        return HttpResponseNotFound("<h2>Grade not found</h2>")
#def about(request):
	#return render(request, "about.html", {"menu": menu})


class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	filterset_class = CourseFilterSet

class TopicViewSet(viewsets.ModelViewSet):
	queryset = Topic.objects.all()
	serializer_class = TopicSerializer
	filterset_class = TopicFilterSet

class HomeworkViewSet(viewsets.ModelViewSet):
	queryset = Homework.objects.all()
	serializer_class = HomeworkSerializer
	filterset_class = HomeworkFilterSet

class GradeViewSet(viewsets.ModelViewSet):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializer


	

