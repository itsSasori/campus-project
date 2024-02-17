from django.urls import path
from . import views

urlpatterns =[
    path('aboutus/',views.about_us,name="aboutus"),
    path('message/',views.messages,name="msg"),
    path('secondmessage/',views.secondmessage,name="smsg"),
    path('b_members/',views.b_members,name="b-members"),
    path('a_members/',views.a_members,name="a-members"),
    path('p_members/',views.p_members,name="p-members"),
]
