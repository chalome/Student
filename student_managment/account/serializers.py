from rest_framework.serializers import ModelSerializer
from account.models import CustomUser

class CustomUserSerializer(ModelSerializer):
	class Meta:
		model=CustomUser
		fields=['username','email','password','profile_photo']