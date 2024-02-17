from django.shortcuts import render
from django.http import HttpResponse
from program.models import Courses

# Create your views here.
def home(request):
    courses = Courses.objects.all()
    context={'courses':courses}
    return render(request,'index.html',context)


def menu(request):
    courses = Courses.objects.all()
    context={'courses':courses}
    return render(request,'base.html',context)

