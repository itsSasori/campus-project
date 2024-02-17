from django.shortcuts import render
from .models import *
from program.models import *
# Create your views here.
def about_us(request):
    course = Courses.objects.all()
    context = {'courses':course}
    return render(request,'aboutus/about-us.html',context)

def messages(request):
    course = Courses.objects.all()
    context = {'courses':course}
    return render(request,'aboutus/message.html',context)

def secondmessage(request):
    course = Courses.objects.all()
    context = {'courses':course}
    return render(request,'aboutus/secondmessage.html',context)

def a_members(request):
    course = Courses.objects.all()
    context = {'courses':course}
    return render(request,'aboutus/a-members.html',context)

def b_members(request):
    course = Courses.objects.all()
    members = BoardMembers.objects.all()
    context={'members':members,'courses':course}
    return render(request,'aboutus/b-members.html',context)

def p_members(request):
    course = Courses.objects.all()
    context = {'courses':course}    
    return render(request,'aboutus/p-members.html',context)
