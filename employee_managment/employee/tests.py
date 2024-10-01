from django.test import TestCase
from .models import *

class ServiceTest(TestCase):

	def setup(self):
		self.service=Service.objects.create(name='music',description='for dance')

	def test_service_creation(self):
		self.assertEqual(self.service.name, 'music')
		self.assertEqual(self.service.description, 'for dance')

	def test_str_method(self):
		self.assertEqual(str(self.service),'music')