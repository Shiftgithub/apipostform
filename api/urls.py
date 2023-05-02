from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student/add', views.StudentViewSet, basename='student')
router.register('teacher/add', views.TeacherViewSet, basename='teacher')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]
