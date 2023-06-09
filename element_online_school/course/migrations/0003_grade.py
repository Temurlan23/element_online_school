# Generated by Django 4.1.7 on 2023-05-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_homework_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, verbose_name='Оценка')),
                ('topic', models.CharField(max_length=255, verbose_name='Тема')),
                ('student', models.CharField(max_length=255, verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Успеваемость студента',
                'verbose_name_plural': 'Успеваемости студентов',
            },
        ),
    ]
