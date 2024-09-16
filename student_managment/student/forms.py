from django import forms
from student.models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=['first_name','last_name','age','gender','profile_photo']