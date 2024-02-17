from django.urls import path
from . import views

urlpatterns =[
    path('',views.notice,name="notices"),
    path('get_notices/',views.get_notices,name="get_notices"),
    path('get_news/',views.get_news,name="get_news"),
    path('notice_detail/<int:pk>/',views.notice_detail,name="notices-detail"),
    path('news_detail/<int:pk>/',views.news_detail,name="news-detail"),

]
