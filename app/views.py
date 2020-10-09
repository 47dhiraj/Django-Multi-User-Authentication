from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm		
from django.contrib.auth import authenticate, login, logout		
from django.contrib import messages		
from .models import *

from .forms import CreateClientForm, CreateAdminForm



# Create your views here.

def clientregisterPage(request):
	form = CreateClientForm()

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'client'
		return super().get_context_data(**kwargs)

	if request.method == 'POST':
		form = CreateClientForm(request.POST)

		if form.is_valid():
			user = form.save()			
			username = form.cleaned_data.get('username')		
			messages.success(request, 'Account was created for ' + username)		
			return redirect('login')		
		

	context = {'form':form}
	return render(request, 'app/register.html', context)



def adminregisterPage(request):
	form = CreateAdminForm()

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'admin'
		return super().get_context_data(**kwargs)

	if request.method == 'POST':
		form = CreateAdminForm(request.POST)

		if form.is_valid():
			user = form.save()			
			username = form.cleaned_data.get('username')		

			messages.success(request, 'Account was created for ' + username)		

			return redirect('adminhome')		
		

	context = {'form':form}
	return render(request, 'app/register.html', context)





def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:	
			login(request, user)	

			if request.user.is_client:
				return redirect('clienthome')
			else:
				return redirect('adminhome')

		else:
			messages.info(request, 'Username OR password is incorrect')		
	
	
	context = {}
	return render(request, 'app/login.html', context)




def clienthome(request):
	context = {}
	return render(request, 'app/clienthome.html', context)


def adminhome(request):
	context = {}
	return render(request, 'app/adminhome.html', context)


def logoutall(request):
	logout(request)	
	return redirect('login')	
