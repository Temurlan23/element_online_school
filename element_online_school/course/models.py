from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
#from users.models import User
#from django.contrib.auth import get_user_model

#User = get_user_model()

class Course(models.Model):
	title = models.CharField(max_length=255, verbose_name="Название")
	start_date = models.DateField(blank=True, null=True, verbose_name="Дата начала курса")
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Курс"
		verbose_name_plural = "Курсы"

class Topic(models.Model):
	title = models.CharField(max_length=255, verbose_name="Название")
	duration = models.DateTimeField(verbose_name="Длительность")
	author = models.OneToOneField("users.User", blank=True, null=True, on_delete=models.CASCADE, verbose_name="Автор")
	course = models.OneToOneField(Course,on_delete=models.CASCADE, verbose_name="Курс")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Тема"
		verbose_name_plural = "Темы"

class Homework(models.Model):
	decision = models.TextField(blank=True, null=True, verbose_name="Решение")
	title = models.CharField(max_length=255, verbose_name="Название")
	complexity = models.CharField(max_length=255, blank=True, null=True, verbose_name="Сложность")
	topic = models.OneToOneField(Topic, on_delete=models.CASCADE, verbose_name="Тема")
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Домашнее задание"
		verbose_name_plural = "Домашние задания"
	

class Grade(models.Model):
	rating = models.PositiveIntegerField(default=0, verbose_name="Оценка")
	topic = models.OneToOneField(Topic, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Тема")
	student = models.OneToOneField("users.User", on_delete=models.CASCADE, verbose_name="Студент")

	def __str__(self):
		return self.student.phone

	class Meta:
		verbose_name = "Успеваемость студента"
		verbose_name_plural = "Успеваемости студентов"

