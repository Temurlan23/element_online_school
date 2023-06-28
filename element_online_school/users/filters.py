import django_filters
from django_filters import filters
from .models import User

class UserFilterSet(django_filters.FilterSet):
	last_name = django_filters.CharFilter(lookup_expr='icontains')
	first_name = django_filters.CharFilter(lookup_expr='icontains')
	middle_name = django_filters.CharFilter(lookup_expr='icontains')
	phone = django_filters.CharFilter(lookup_expr='icontains')
	city = django_filters.CharFilter(lookup_expr='icontains')
	role = django_filters.CharFilter(lookup_expr='icontains')
	birth_date_year = django_filters.NumberFilter(field_name='birth_date', lookup_expr='year')
	course__title = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = User
		fields = ('last_name','first_name','middle_name','phone','city','role','is_staff','is_superuser','course__title','birth_date',)