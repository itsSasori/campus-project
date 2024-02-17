from django.shortcuts import render,redirect
from .forms import *
from program.models import *
# Create your views here.
def contact(request):
    course = Courses.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    context={'form':form,'courses':course}
    return render(request,'contact/contact.html',context)

            
