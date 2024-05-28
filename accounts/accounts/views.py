from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def signup_view(request, backend='django.contrib.auth.backends.ModelBackend'):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			#log user in
			login(request, user, backend='django.contrib.auth.backends.ModelBackend')
			return redirect('/home')
	else:
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {
		'form': form
		})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log in the user
			user = form.get_user()
			login(request, user)
			messages.info(request, "Successfully Signed In!")
			return redirect('/home')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {
		'form': form
		})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		messages.info(request, "Successfully Signed Out!")
		return redirect('/home')
