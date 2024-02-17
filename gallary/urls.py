from django.urls import path
from . import views

urlpatterns =[
    path('',views.gallary,name="gallary"),
    path('m_gallary',views.main_gallary,name="main_gallary"),
    path('m_gallary_detail/<int:pk>/',views.main_gallary_detail,name="main_gallary-detail"),
    path('gallery_detail/<int:pk>/',views.gallary_detail,name="gallary-detail"),
    path('g-downloads',views.g_downloads,name="g-downloads")
]
