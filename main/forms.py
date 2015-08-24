from django import forms
from main.models import SpeedModel

class SpeedModelForm(forms.ModelForm):
	class Meta:
		model = SpeedModel
		fields = '__all__'


class SpeedModelForm2(forms.Form):
	title = forms.CharField(required=True)
	info = forms.CharField(required=True, widget=forms.Textarea)
	image = forms.ImageField(required=True)
	user = forms.CharField(required=False, widget=forms.HiddenInput)

class SpeedModelUpdateForm(forms.Form):
	title = forms.CharField(required=True)
	info = forms.CharField(required=True, widget=forms.Textarea)
	image = forms.ImageField(required=False)


class UserSignUp(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class UserLogIn(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())