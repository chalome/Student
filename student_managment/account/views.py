from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from account.forms import LoginForm,SignUpForm
from account.models import CustomUser
from django.contrib.auth import login,logout
from django.conf import settings
from django.views import View
from rest_framework import status
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from account.serializers import CustomUserSerializer
class home(TemplateView):
	template_name='account/home.html'

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    authentication_form = LoginForm  # Use your custom form
    extra_context = {'message': ''}  # Optional: you can set default context here

    def form_invalid(self, form):
        # Optionally, you can customize the error message here
        self.extra_context['message'] = 'Invalid Identifiers.'
        return super().form_invalid(form)

class SingUpView(CreateView):
	template_name='account/signup.html'
	form_class=SignUpForm
	model=CustomUser
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user = form.save()
        # Auto-login the user after successful registration
		login(self.request, user)
		return redirect(settings.LOGIN_REDIRECT_URL)

	def form_invalid(self, form):
		message = 'Erreur'
		return self.render_to_response({'form': form, 'message': message})

class CustomLogoutView(View):
	def get(self, request):
		logout(request)
		return redirect('login')

class CustomUserViewSet(ModelViewSet):
	queryset=CustomUser.objects.all()
	serializer_class=CustomUserSerializer

	# def list(self,request):
	# 	queryset=self.get_queryset()
	# 	serializer=self.get_serializer(queryset,many=True)
	# 	return Response(serializer.data)


