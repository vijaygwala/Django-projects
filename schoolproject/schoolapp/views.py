from django.shortcuts import render
from schoolapp.models import StudentInfo
def Schoolbs(request):
    return render(request,'pages/schoolbs.html')
def Aboutus(request):
    return render(request,'pages/aboutus.html')
def Transfer(request):
    return render(request,'pages/transfer.html')
def Contactus(request):
    return render(request,'pages/contactus.html')
def Gallary(request):
    return render(request,'pages/portfolio.html')
def Message(request):
    return render(request,'pages/message.html')
def Facilities(request):
    return render(request,'pages/facilities.html')
def Notice(request):
    return render(request,'pages/noticebord.html')
def dbtable(request):
    #studentdb=Student.objects.all()
    enrollm=request.GET['enroll']
    studentdb=StudentInfo.objects.filter(enroll=enrollm)
    #studentdb=Student.objects.filter(marks__lt=35)
    #studentdb=Student.objects.filter(sname__startswith='A')
    #studentdb=Student.objects.all().order_by('marks')
    #studentdb=Student.objects.all().order_by('-marks')

    return render(request,'pages/studentinfo.html',{'studentdb':studentdb})
