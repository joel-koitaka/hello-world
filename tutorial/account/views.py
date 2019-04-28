from django.shortcuts import render,redirect  # render is used to render html templates
# from django.contrib.auth.forms import UserCreationForm
from account.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

# Create your views here.
def home(request):
	args={'user': request.user}
	return render(request, 'account/home.html', args) 

def back_home(request):
	args = {'user': request.user}
	return redirect('/home', args)
   
	#return render(request, 'account/home.html', args)  
	# return HttpResponse('Home Page!') 
	#above code is rewritten using render method
def register(request):
	if request.method =='POST':  #post sends data to be server
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = RegistrationForm()

		args = {'form': form}
		return render(request, 'account/reg_form.html', args)
def view_profile(request):
	args ={'user': request.user}
	return render (request, 'account/profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid:
			form.save()
			return redirect('/account/profile')
	else:
		form = EditProfileForm(instance=request.user)
		args= {'form': form}
		return render(request, 'account/edit_profile.html', args)
def change_password(request):
	if request.method=='POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid:
			form.save()
			return redirect('/account/profile')
	else: 
		form=PasswordChangeForm(user=request.user)
		args= {'form': form}
		return render(request, 'account/change_password.html', args)

def workstations1(request):
	args ={'user': request.user}
	return render (request, 'account/workstations1.html', args)
def workstations2(request):
	args ={'user': request.user}
	return render (request, 'account/workstations2.html', args)

def experiment1(request):
	args ={'user': request.user}
	return render (request, 'account/experiment1.html', args)
def experiment2(request):
	args ={'user': request.user}
	return render (request, 'account/experiment2.html', args)
def experiment3(request):
	args ={'user': request.user}
	return render (request, 'account/experiment3.html', args)
def about(request):
	args ={'user': request.user}
	return render (request, 'account/about.html', args)

def media(request):
	args ={'user': request.user}
	return render (request, 'account/media', args) #used to acces pdf files upload in django admin
	 
	 







