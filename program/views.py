from django.shortcuts import render
from .models import *
from notices.models import *

# Create your views here.

def courses_detail(request,pk):
    coursed=Courses.objects.get(id=pk)
    course = Courses.objects.all()
    bbayear1 = BBAFeeStructureYear1.objects.filter(course=coursed)
    bbayear2 = BBAFeeStructureYear2.objects.filter(course=coursed)
    bbayear3 = BBAFeeStructureYear3.objects.filter(course=coursed)
    bbayear4 = BBAFeeStructureYear4.objects.filter(course=coursed)
    bbsyear1 = BBSFeeStructureYear1.objects.filter(course=coursed)
    model_fields = BBAFeeStructureYear1._meta.get_fields()
    field_names = [field.name for field in model_fields if field.name != 'id' and field.name != 'course']  # Exclude 'id' field if you want
    notices = Notices.objects.all()[0:5]
    news = News.objects.all()[0:5]
    context={'bbsyear1':bbsyear1,'bbayear1':bbayear1,'bbayear3':bbayear3,'bbayear4':bbayear4,'bbayear2':bbayear2,'model_fields':model_fields,'field_names':field_names,'notices':notices,'news':news,'course':coursed,'courses':course}
    return render(request,'program/course-detail.html',context)










