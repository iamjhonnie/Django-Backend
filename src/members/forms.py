from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=50)


    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name', 
            'password1', 
            'password2')

    def __init__(self, *args: Any, **kwargs: Any):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'