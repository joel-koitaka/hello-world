from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistratonForm(UserCreationForm):
	email = forms.EmailField (required=True)

	class Meta:
		model =User
		fields = (
			'username',
			"first_name",
			'last_name',
			'email',
			'password1',
			'password2',

			)
	def save(self, commit=True)
	user = super(RegistratonForm, self).save(commit=False)
	user.first_name = cleaned.data ['first_name']
	user.last_name = cleaned.data['last_name']
	user.email = cleaned.data['email']

	if commit:
		user.save()
	return user