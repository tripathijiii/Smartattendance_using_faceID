from decimal import Context
from django.shortcuts import redirect, render,HttpResponse
from .models import student
from .recognition import facerecognition
from .excelupdation import getstudentdetails,newstudentexcel,mailexcel
import os
# Create your views here.
flag=0
def authenticate(request):
    if request.method=='POST':
        global flag
        name=request.POST.get('name')
        password=request.POST.get('pass')
        if(name =='admin' and password =='admin'):
            flag=1
            return render(request,'Face/choices.html')
        else:
            return HttpResponse("wait a min, WHO ARE YOU ")
    return render(request,'Face/page2.html')

def index(request):
    global flag
    flag=0
    if request.method=='POST':
        name = request.POST.get('name',)
        roll = request.POST.get('roll',)
        image=request.FILES['image']
        a=student(name=name,roll=roll,image=image)
        a.save()
        d= facerecognition(name,roll)
        if d=={}:
            return HttpResponse("ATTENDANCE NOT MARKED")
        return render(request,"Face/attendance_marked.html",d)
    return render(request,'Face/page.html')

def newstudent(request):
    global flag
    if request.method=='POST':
        name = request.POST.get('name',)
        roll = request.POST.get('roll',)
        email = request.POST.get('email',)
        image=[]
        image.append(request.FILES['image1'])
        img_extension = os.path.splitext(image[0].name)
        user_folder = '/Users/shashwateshtripathi/Desktop/SE/SE/Face/studentface/{}'.format(name.upper())
        
        if not os.path.exists(user_folder):
            os.mkdir(user_folder)
            newstudentexcel(name,roll,email)

        else:
            return render(request,"Face/user.html")
        c=0
        for i in image:
            img_save_path="{}/{}{}".format(user_folder,"omghfgds",".jpeg")
            with open(img_save_path, 'wb+') as f:
                for chunk in i.chunks():
                    f.write(chunk)
            c+=1
        return render(request,"Face/loggedin.html")
    if flag==1:
        return render(request,"Face/newstudent.html")
    else:
        return HttpResponse("Sign in as admin first")


def attendancedetails(request):
    details,count = getstudentdetails()
    if request.method=='POST':
        name = request.POST.get('search',)
        dict={}
        for i in details:
            if i==name:
                dict[i]=details[i]
        return render(request,"Face/stud_details.html",{'details':dict})
    return render(request,"Face/stud_details.html",{'details':details,'count':count})


def defaulters(request):
    if request.method=='POST':
        boundary=request.POST.get('percentage',)
        mailexcel(boundary)
        return redirect('/authenticate')
    return render(request,"Face/defaulter.html")