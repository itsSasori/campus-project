from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import *
from program.models import *

# Create your views here.

def notice(request):
    return HttpResponse("ALL Notices")

def get_notices(request):
    notices = Notices.objects.all()
    news =News.objects.all()
    courses = Courses.objects.all()
    context={'notices':notices,'news':news,'courses':courses}
    return render(request,'notices/notices.html',context)

def get_news(request):
    notices = Notices.objects.all()
    news =News.objects.all()
    courses = Courses.objects.all()
    context={'notices':notices,'news':news,'courses':courses}
    return render(request,'notices/news.html',context)


def notice_detail(request,pk):
    notice = Notices.objects.get(id=pk)
    course = Courses.objects.all()
    news = News.objects.all()
    context={'notice':notice,'news':news,'courses':course}
    return render(request,'notices/notices-detail.html',context)


def news_detail(request,pk):
    news = News.objects.get(id=pk)
    notice = Notices.objects.all()
    course = Courses.objects.all()
    context={'news':news,'courses':course,'notices':notice}
    return render(request,'notices/news-detail.html',context)