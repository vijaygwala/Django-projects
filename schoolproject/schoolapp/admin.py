from django.contrib import admin
from schoolapp.models import StudentInfo



class StudentInfoAdmin(admin.ModelAdmin):
    list_display=['id','enroll','sname','img','sclass','saddr','status','fatherName','motherName','DOB','enrollDate','sid','gender','nationality']
admin.site.register(StudentInfo,StudentInfoAdmin)
# Register your models here.
