from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def first(request):
    return HttpResponse("<h1> welcome </h1>"
                        "<p> this is a paragraph</p>")

def second(request):
    return render(request,"first.html")

def reg(request):
    if request.method=='POST':
        a=reform(request.POST)
        if a.is_valid():
            us=a.cleaned_data["username"]
            em=a.cleaned_data["email"]
            ph=a.cleaned_data["phone"]
            ps=a.cleaned_data["password"]
            cp=a.cleaned_data["confirmpassword"]
            if ps==cp:
                b=regmodel(username=us,email=em,phone=ph,password=ps)
                b.save()
                return HttpResponse("registration success")
            else:
                return HttpResponse("password doesn't match")
        else:
            return HttpResponse("registration failed")
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            us=a.cleaned_data["username"]
            ps=a.cleaned_data["password"]
            b=regmodel.objects.all()
            for i in b:
                if us==i.username and ps==i.password:
                    return HttpResponse("Login success")
            else:
                return HttpResponse("Login failed")
    return render(request,"login.html")

def emp(request):
    if request.method=='POST':
        a=empform(request.POST)
        if a.is_valid():
            en=a.cleaned_data["employee_name"]
            ei=a.cleaned_data["employee_id"]
            cn=a.cleaned_data["company_name"]
            em=a.cleaned_data["email"]
            dp=a.cleaned_data["department"]
            b=empmode(employee_name=en,employee_id=ei,company_name=cn,email=em,department=dp)
            b.save()
            return HttpResponse("employee added")
        else:
            return HttpResponse("registration failed")
    return render(request,"employee.html")


def search(request):
    if request.method=='POST':
        a=searchform(request.POST)
        if a.is_valid():
            en=a.cleaned_data["employee_name"]
            ei=a.cleaned_data["employee_id"]
            b=empmode.objects.all()
            for i in b:
                if en==i.employee_name and ei==i.employee_id:
                    return HttpResponse("employee found")
            return HttpResponse("employee not found")
    return render(request,"search.html")

def display(request):
    a=regmodel.objects.all()
    return render(request,"display.html",{'a':a})

def empdisplay(request):
    a=empmode.objects.all()
    return render(request,"empdisplay.html",{'a':a})

def imageupload(request):
    if request.method=='POST':
        a=imgform(request.POST,request.FILES)
        if a.is_valid():
            im=a.cleaned_data["imgname"]
            fl=a.cleaned_data["imgfile"]
            b=imgmodel(imgname=im,imgfile=fl)
            b.save()
            return HttpResponse("image upload successfully...")
        else:
            return HttpResponse("upload failed")
    return render(request,"imageupload.html")

def imagedisplay(request):
    a=imgmodel.objects.all()
    image=[]
    name=[]
    for i in a:
        fl=i.imgfile
        image.append(str(fl).split('/')[-1])
        im=i.imgname
        name.append(im)
    mylist=zip(image,name)
    return render(request,"imagedisplay.html",{'mylist':mylist})

def audioupload(request):
    if request.method=='POST':
        a=audioform(request.POST,request.FILES)
        if a.is_valid():
            an=a.cleaned_data["audname"]
            ai=a.cleaned_data["audimg"]
            af=a.cleaned_data["audfile"]
            b=audiomodel(audname=an,audimg=ai,audfile=af)
            b.save()
            return HttpResponse("upload successfully........")
        else:
            return HttpResponse("upload failed..... ")
    return render(request,"audio.html")


def audiodisplay(request):
    a=audiomodel.objects.all()
    audname=[]
    audimage=[]
    audfile=[]
    for i in a:
        af = i.audfile
        audfile.append(str(af).split('/')[-1])
        ai=i.audimg
        audimage.append(str(ai).split('/')[-1])
        an = i.audname
        audname.append(an)
    mylist=zip(audfile,audimage,audname)
    return render(request,"audiodisplay.html",{'mylist':mylist})

def videoupload(request):
    return render(request,"video.html")


