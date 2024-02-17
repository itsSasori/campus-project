from django.urls import path
from . import views

urlpatterns =[
    path('course-detail/<int:pk>/',views.courses_detail,name="course-detail"),
 
]
