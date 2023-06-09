# Generated by Django 4.1.7 on 2023-05-10 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_grade'),
        ('users', '0003_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('STUDENT', 'Student'), ('TEACHER', 'Teacher'), ('MANAGER', 'Manager')], default='MANAGER', max_length=7, verbose_name='Роль'),
        ),
    ]
