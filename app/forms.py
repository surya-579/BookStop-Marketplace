from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import *
class CustomerRegistrationForm(UserCreationForm):
  password1 = forms.CharField(label= 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2 = forms.CharField(label= 'confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
  email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
  class Meta:
    model = User
    fields = ['username','email','password1','password2']
    label = {'email':'Email'}
    widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
    


class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
  password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs= {'autocomplete':'current-password','class':'form-control'}   ))
  

class MyPasswordChangeForm(PasswordChangeForm):
  old_password = forms.CharField(label=_("old Password"),strip=False,widget=forms.PasswordInput(attrs= {'autocomplete':'current-password','class':'form-control'}))
  
  
  new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs= {'autocomplete':'current-password','class':'form-control'}   ),
  help_text=password_validation.password_validators_help_text_html())
  
  
  new_password2 = forms.CharField(label=_("Confirm Password"),strip=False,widget=forms.PasswordInput(attrs= {'autocomplete':'current-password','class':'form-control'}   ))
  
  
class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['name','rollNumber','phoneNumber','branch']



class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields ="__all__"



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title', 'selling_price', 'discount_price', 'description',
            'category', 'product_img', 'product_imag', 'product_image', 'product_images'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'discount_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'product_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'product_imag': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'product_images': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


        