  
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Link
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class NewMeetingForm(ModelForm):
	class Meta:
		model = Link
		fields = '__all__'
"""
	def __init__(self,*args, **kwargs):
		self.user = kwargs.pop('user')
		super(NewMeetingForm,self).__init__(*args,**kwargs)
	
	def save(self)



    def save(self, commit=True):
        inst = super(NewMeetingForm, self).save(commit=False)
        inst.author = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst """