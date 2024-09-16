from django.shortcuts import render
from django.views.generic import TemplateView

# def home(request):
# 	return render(request,'account/home.html')

class home(TemplateView):
	template_name='account/home.html'
