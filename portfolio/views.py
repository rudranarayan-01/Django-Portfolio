from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Project,Contact

# Create your views here.
def home(request):
    posts=Project.objects.all()
    context={"posts":posts}
    return render(request,'retrive.html',context)



def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")


    return render(request,'retrive.html')


