from django.contrib import admin
from student.models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','age','gender','profile_photo')

admin.site.register(Student,StudentAdmin)