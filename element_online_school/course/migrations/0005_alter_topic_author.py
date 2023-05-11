# Generated by Django 4.1.7 on 2023-05-11 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_remove_course_topic_homework_topic_topic_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
