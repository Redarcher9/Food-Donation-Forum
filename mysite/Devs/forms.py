from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import comment

class registrationform(UserCreationForm):
    """docstring forregistrationform."""
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())


    class Meta:
              model = User
              fields = ('username',
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2',
                    )
class commentform(forms.ModelForm):

    class Meta:
        model = comment
        fields = ('context',)
