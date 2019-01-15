from .models import *
from django import forms
from django.contrib.auth.models import User
class PostCreateForms(forms.ModelForm):
    class Meta:
        model=Posts
        fields=['title','body','status','image']

class UserLoginForm(forms.Form):
    username=forms.CharField(label="Enter your Username")
    password=forms.CharField(label="Enter your Password")


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = (
            'title',
            'body',
            'image',
            'status',


        )

class UserRegistrationForm(forms.ModelForm):

    password=forms.CharField(label='Enter your Password')
    confirm_password=forms.CharField(label='Enter your Password')

    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
        widgets={
            'username':forms.TextInput(attrs={'class':'input'}),
            'first_name':forms.TextInput(attrs={'class':'input'}),
             'last_name':forms.TextInput(attrs={'class':'input'}),
             'email':forms.TextInput(attrs={'class':'input'}),





        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password Mismatch")
        return confirm_password
class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    boi=forms.CharField(widget=forms.Textarea(attrs={'class':'input'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'boi',
        )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=('user',)

class Contact(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput())
    class Meta:
        model=Contact
        fields=['fullname','email','contact','message']
