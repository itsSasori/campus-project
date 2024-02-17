from django.shortcuts import render,redirect
from .models import *
from notices.models import *
from program.models import *
# Create your views here.

def gallary(request):
    course = Courses.objects.all()
    gallary = Gallary.objects.all()
    context={'gallary':gallary,'courses':course}
    return render(request,"gallary/gallary.html",context)

def gallary_detail(request,pk):
    course = Courses.objects.all()
    gallary = Gallary.objects.get(id=pk)
    # form = GallaryImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for image in images:
             # Create a GallaryImage instance without saving it yet
                image_instance = GallaryImage(pic=image)
                # Assign the Gallary instance to the related field
                image_instance.gallary = gallary
                # Save the GallaryImage instance
                image_instance.save()
        return redirect('gallary')
    
    images = GallaryImage.objects.filter(gallary=gallary)
    context={'gallary':gallary,'images':images,'courses':course}
    return render(request,'gallary/gallary-detail.html',context)

def main_gallary(request):
    gallary = MainGallary.objects.all()
    context={'gallary':gallary}
    return render(request,"gallary/main-gallary.html",context)

def main_gallary_detail(request,pk):
    gallary = MainGallary.objects.get(id=pk)
    # form = GallaryImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for image in images:
             # Create a GallaryImage instance without saving it yet
                image_instance = MainGallaryImages(pic=image)
                # Assign the Gallary instance to the related field
                image_instance.main_gallary = gallary
                # Save the GallaryImage instance
                image_instance.save()
        return redirect('main_gallary')
    
    images = MainGallaryImages.objects.filter(main_gallary=gallary)
    context={'gallary':gallary,'images':images}
    return render(request,'gallary/main_gallary-detail.html',context)


def g_downloads(request):
     downloads =Downloads.objects.all()[0:5]
     notices = Notices.objects.all()
     news =News.objects.all()
     print(notices)
     context={"downloads":downloads,'notices':notices,'news':news}
     return render(request,'gallary/downloads.html',context)