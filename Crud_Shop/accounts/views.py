from django.shortcuts import render, get_object_or_404, redirect

from .models import Profile
from shopping_cart.models import Order

from django.contrib.auth import (
	authenticate,
	login,
	logout
)

from .forms import (
	UserLoginForm,
	UserRegistrationForm
)
#this entire section uses the Django built in Authentication framework to easily create a user system
#This redirects the user if the correct login is given
def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password = password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect('/products')
	context = {
		'form': form,
	}
	return render(request, "login.html", context)

#this saves the data into the database
def register_view(request):
	next = request.GET.get('next')
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect('/products')
	context = {
		'form': form,
	}
	return render(request, "register.html", context)

#login
def logout_view(request):
	logout(request)
	return redirect('/login')

def my_profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
	context = {
		'my_orders': my_orders
	}

	return render(request, "profile.html", context)