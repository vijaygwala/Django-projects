from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    enroll=models.CharField(unique=True,max_length=30)
    sname=models.CharField(max_length=64)
    img=models.ImageField(upload_to='pics')
    sclass=models.CharField(max_length=64)
    saddr=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    fatherName=models.CharField(max_length=100)
    motherName=models.CharField(max_length=100)
    DOB=models.DateField()
    enrollDate=models.DateField()
    sid=models.CharField(unique=True,max_length=30)
    gender=models.CharField(max_length=10)
    nationality=models.CharField(max_length=30)
