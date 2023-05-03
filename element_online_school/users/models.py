from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
	last_name = models.CharField(max_length=255, verbose_name="Фамилия")
	first_name = models.CharField(max_length=255, verbose_name="Имя")
	middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отчество")
	birth_date = models.DateField(blank=True, null=True, verbose_name="Дата рождение")
	phone = models.CharField(max_length=255,unique=True,verbose_name="Номер телефона")
	city = models.CharField(max_length=255, blank=True, null=True, verbose_name="Город")
	is_staff = models.BooleanField(default=False, verbose_name="Сотрудник")
	is_superuser = models.BooleanField(default=False, verbose_name="Суперпользователь")

	objects = UserManager()
	USERNAME_FIELD = "phone"

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = "Пользователь"
		verbose_name_plural = "Пользователи"