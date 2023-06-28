from django.urls import path
from .views import CourseViewSet, TopicViewSet, HomeworkViewSet, GradeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'topic', TopicViewSet, basename='topic')
router.register(r'homework', HomeworkViewSet,basename='homework')
router.register(r'grade', GradeViewSet, basename='grade')

urlpatterns = router.urls