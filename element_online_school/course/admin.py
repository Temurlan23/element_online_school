from django.contrib import admin
from .models import Course, Topic, Homework, Grade
from django.contrib import admin


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','start_date')
    #raw_id_fields = ('id',)
    readonly_fields = ('id',)

admin.site.register(Course, CourseAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','duration','author','course')
    #raw_id_fields = ('id',)
    readonly_fields = ('id',)

admin.site.register(Topic, TopicAdmin)

class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','decision','complexity','topic')
    #raw_id_fields = ('id',)
    readonly_fields = ('id',)

admin.site.register(Homework, HomeworkAdmin)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating','topic','student')
    #raw_id_fields = ('id',)
    readonly_fields = ('id',)

admin.site.register(Grade, GradeAdmin)

