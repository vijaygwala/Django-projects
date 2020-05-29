import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolproject.settings')
import django
django.setup()

from schoolapp.models import *
from faker import Faker
from random import *
faker=Faker()
def fakedb(n):
    for i in range(n):
        feno=randint(1001,9999)
        fname=faker.name()
        fclass=fake.random_element(elements=('11th-science','12th-Science','11th-commerce','12th-commerce','10th'))
        faddr=fake.address()
        student_record=Student.objects.get_or_create(eno=feno,sname=fname,sclass=fclass,saddr=faddr)
fakedb(10)
