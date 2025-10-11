from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('courses/', views.courses_list),
    path('courses/<int:course_id>/', views.course_detail),
]