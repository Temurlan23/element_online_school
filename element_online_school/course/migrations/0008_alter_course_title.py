# Generated by Django 4.1.7 on 2023-06-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_grade_topic_alter_homework_complexity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
    ]