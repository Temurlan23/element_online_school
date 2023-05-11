from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager
from course.models import Course


# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
	ROLE_CHOICES = (
		('STUDENT','Student'), 
		('TEACHER','Teacher'),
		('MANAGER','Manager'),
	)

	last_name = models.CharField(max_length=255, verbose_name="Фамилия")
	first_name = models.CharField(max_length=255, verbose_name="Имя")
	middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отчество")
	birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождение")
	phone = models.CharField(max_length=255,unique=True,verbose_name="Номер телефона")
	city = models.CharField(max_length=255, blank=True, null=True, verbose_name="Город")
	is_staff = models.BooleanField(default=False, verbose_name="Сотрудник")
	is_superuser = models.BooleanField(default=False, verbose_name="Суперпользователь")
	course = models.ForeignKey(Course, on_delete = models.CASCADE,blank=True,null=True, verbose_name="Курс")
	role = models.CharField(max_length=7, choices=ROLE_CHOICES, default="MANAGER",verbose_name="Роль")

	objects = UserManager()
	USERNAME_FIELD = "phone"

	def __str__(self):
		return self.phone

	class Meta:
		verbose_name = "Пользователь"
		verbose_name_plural = "Пользователи"


