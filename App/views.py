from django.shortcuts import render,HttpResponseRedirect
from App.models import Information
from App.forms import infoForm
from django.contrib import messages
from django.urls import reverse

 
 
def home(request):
    blog_info=Information.objects.all()
    form=infoForm()
    if request.method=='POST':
        form=infoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Information addes successfully !")
            return HttpResponseRedirect(reverse('App:home'))
    return render(request,'App/home.html',context={'form':form,'blog_info':blog_info})


 