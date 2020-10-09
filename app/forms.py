from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm		
from django.contrib.auth.models import User			
from django import forms			
from django.db import transaction
from .models import *

class CreateClientForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {"username": None,
                      "email": None,
                      "password2": None                      
                    }       

    @transaction.atomic                 
    def save(self):
        user = super().save(commit=False) 
        user.is_client = True            
        user.is_admin = False
        user.save()       
        
        return user



class CreateAdminForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email':'Email',
            'password1':'Password',
            'password2':'Re-Password'
        }
        help_texts = {"username": None,
                      "email": None,
                      "password2": None                      
                    } 
                    
    @transaction.atomic  
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True 
        user.save()
        return user



