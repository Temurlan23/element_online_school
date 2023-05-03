from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class Course(models.Model):
	title = models.CharField(max_length=255, verbose_name="Название")
	start_date = models.DateField(blank=True, null=True, verbose_name="Дата начала курса")
	topic = models.CharField(max_length=255, verbose_name="Тема")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Курс"
		verbose_name_plural = "Курсы"
	
