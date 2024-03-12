from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm): #new register form
    class Meta:
        model=User
        fields=('username','email','password1','password2')
          
class LoginUserForm(AuthenticationForm): #login its authntication
    class Meta:
        model=User
        fields={'username','password'}

        # labels={
        #     'name':'Enter your username',
        #     'password':'Enter your password',
        # }
        # widgets={
        #     'name':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
        #     'password':forms.TextInput(attrs={'class':'form-control'}),
        # }



