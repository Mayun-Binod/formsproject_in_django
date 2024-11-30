import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","formsproject.settings")
import django
django.setup()
from faker import Faker 
from random import *
from firstapp.models import Employee 

faker = Faker("ne_NP")
def dataFaker(n):
    for i in range(n):
        feno = randint(1,100000)
        fename = faker.name()
        fesal = randint(10000,10000000)
        feaddr = faker.city()
        emp_record = Employee.objects.create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
dataFaker(11)