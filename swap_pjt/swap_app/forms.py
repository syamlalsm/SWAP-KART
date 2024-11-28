from django.contrib.auth.forms import UserCreationForm
from . models import *
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = BrandModel
        fields = ['model_name', 'name', 'image', 'year', 'kilometer', 'engine', 'actual_price', 'booking_price', 'location', 'description']
