from django import forms

from businessapp.models import Employee

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		# fields = ['name','mobile','salary']
		fields = "__all__"	
	