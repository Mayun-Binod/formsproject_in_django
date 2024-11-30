from django.shortcuts import render
from firstapp.models import Employee
# Create your views here.
def index(request):
    my_obj=Employee.objects.all()
    context={'my_obj':my_obj}
    return render(request,'firstapp/index.html',context=context)
