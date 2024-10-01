from rest_framework.serializers import ModelSerializer
from .models import Service,Category,Employee
from rest_framework import serializers

class CategoryDetailSerializer(ModelSerializer):
	employees=serializers.SerializerMethodField()
	class Meta:
		model=Category
		fields=['id','name','description','employees']
	def get_employees(self,instance):
		queryset=instance.employees.filter(working=True)
		serializer=EmployeeSerializer(queryset,many=True)
		return serializer.data

class CategoryListSerializer(ModelSerializer):
	class Meta:
		model=Category
		fields=['id','name','description']

class ServiceDetailSerializer(ModelSerializer):
	employees = serializers.SerializerMethodField()
	class Meta:
		model=Service
		fields=['id','name','description','active','employees']

	def get_employees(self, instance):
		queryset = instance.employees.filter(working=True)
		serializer = EmployeeSerializer(queryset, many=True)
		return serializer.data

class ServiceListSerializer(ModelSerializer):
	class Meta:
		model=Service
		fields=['id','name','description','active']

class EmployeeSerializer(ModelSerializer):
	class Meta:
		model=Employee
		fields='__all__'