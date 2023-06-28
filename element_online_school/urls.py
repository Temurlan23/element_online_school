"""
URL configuration for element_online_school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

#from users import views
from course import views


urlpatterns = [
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('topic/', views.topic),
    path('', views.course),
    #path('', views.topic),
    #path('', views.homework),
    path('topic/create_topic/', views.create_topic),
    path('topic/edit_topic/<int:id>/', views.edit_topic),
    path('topic/delete/<int:id>/', views.delete_topic),
    path('homework/', views.homework),
    path('create_homework/', views.create_homework),
    path('homework/edit_homework/<int:id>/', views.edit_homework),
    path('homework/delete/<int:id>/', views.delete_homework),
    path('grade/', views.grade),
    path('grade/create_grade/', views.create_grade),
    path('grade/edit_grade/<int:id>/', views.edit_grade),
    path('grade/delete/<int:id>/', views.delete_grade),    
    path('about/',views.about),
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/course/', include('course.urls'))

]
