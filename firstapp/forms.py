from django import forms
from firstapp.models import Employee
# class EmployeeForm(forms.Form):
#     ename = forms.CharField()
#     eaddr = forms.CharField()
#     eno=forms.IntegerField()
#     esal=forms.FloatField()

class EmployeeForm(forms.ModelForm):
    # validators code you can write here...
    class Meta:
        model=Employee
        fields="__all__"
        widgets={'ename':forms.TextInput(attrs={'class':'form-control','placeholder':"enter you name here:"})}