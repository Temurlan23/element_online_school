from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name','first_name','middle_name','birth_date','phone',
    				'city','is_staff','is_superuser','course','role')
    #raw_id_fields = ('id',)
    readonly_fields = ('id',)


admin.site.register(User, UserAdmin)
