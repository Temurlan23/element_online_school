import django_filters
from .models import Course, Topic, Homework

class CourseFilterSet(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_expr='icontains')
	start_date = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Course
		fields = ('title','start_date',)

class TopicFilterSet(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_expr='icontains')
	duration  = django_filters.NumberFilter(field_name='duration', lookup_expr='year')
	author__first_name = django_filters.CharFilter(lookup_expr='icontains')
	author__last_name = django_filters.CharFilter(lookup_expr='icontains')
	author__middle_name = django_filters.CharFilter(lookup_expr='icontains')
	course__title = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Topic
		fields = ('title','duration','author','course',)

class HomeworkFilterSet(django_filters.FilterSet):
	decision = django_filters.CharFilter(lookup_expr='icontains')
	title = django_filters.CharFilter(lookup_expr='icontains')
	complexity = django_filters.CharFilter(lookup_expr='icontains')
	topic__title = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Homework
		fields = ('title','complexity','decision','topic',)
