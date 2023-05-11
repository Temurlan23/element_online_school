# Generated by Django 4.1.7 on 2023-05-11 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0006_alter_grade_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='topic',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.topic', verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='complexity',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Сложность'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='decision',
            field=models.TextField(blank=True, null=True, verbose_name='Решение'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='duration',
            field=models.DateTimeField(verbose_name='Длительность'),
        ),
    ]
