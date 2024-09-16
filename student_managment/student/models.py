from django.db import models

class Student(models.Model):
	class Gender(models.TextChoices):
		MALE='MALE','Male'
		FEMALE='FEMALE','Female'

	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	age=models.IntegerField(verbose_name='Age')
	gender=models.CharField(max_length=10,choices=Gender,verbose_name='Gender')
	profile_photo=models.ImageField(verbose_name='Profile Photo')

	def __str__(self):
	 	return self.last_name

