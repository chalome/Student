from django.db import models,transaction

class Service(models.Model):
	name=models.CharField(max_length=255)
	description=models.TextField(blank=True)
	active=models.BooleanField(default=True)

	def __str__(self):
		return self.name

	@transaction.atomic
	def disable(self):
		if self.active is True:
			return
		self.active=True
		self.save()
		self.employees.update(working=True)
     
     

class Category(models.Model):
	name=models.CharField(max_length=255)
	description=models.TextField(blank=True)
	def __str__(self):
		return self.name

class Employee(models.Model):
	fname=models.CharField(max_length=255,verbose_name='First Name')
	lname=models.CharField(max_length=255,verbose_name='Last Name')
	birth_year=models.PositiveIntegerField()
	service=models.ForeignKey(Service, on_delete=models.CASCADE,related_name="employees")
	salary=models.PositiveIntegerField()
	category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name="employees")
	cin=models.CharField(max_length=255)
	photo=models.ImageField(blank=True)
	working=models.BooleanField(default=True)

	def __str__(self):
		return f'{self.fname} {self.lname}'

