#coding: utf8
from django.contrib.auth.forms import AuthenticationForm

class MyAuthenticationForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(MyAuthenticationForm, self).__init__(*args, **kwargs)

		self.base_fields['username'].widget.attrs['class'] = 'form-control mr-sm-2'
		self.base_fields['password'].widget.attrs['class'] = 'form-control mr-sm-2'	
		self.base_fields['username'].widget.attrs['placeholder'] = 'Username'
		self.base_fields['password'].widget.attrs['placeholder'] = 'Password'	

