from django.contrib import admin
from account.models import CustomUser

class UserAdmin(admin.ModelAdmin):
	list_display=('email','password','profile_photo')
admin.site.register(CustomUser,UserAdmin)
