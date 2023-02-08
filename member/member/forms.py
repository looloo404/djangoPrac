from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyMemberForm(UserCreationForm):

    # UserCreationForm 'username, password1,password2,lastname
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        model = User 
        fields = ('username', 'password1','password2','email','first_name','last_name')

