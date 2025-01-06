from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import Blogs
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('Blog_title',  'Blog_content', )
        widgets = {
            'Blog_title': forms.TextInput(attrs={
                
            }),
            
            'Blog_content': forms.Textarea(attrs={
                
            }),
            
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ('Blog_title', 'Blog_author', 'Blog_content', )
        widgets = {
            'Blog_title': forms.TextInput(attrs={
                
            }),
            'Blog_author': forms.TextInput(attrs={
                
            }),
            'Blog_content': forms.Textarea(attrs={
                
            }),
            
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'docid','password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    docid = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Doctor ID',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))


class SignupForm1(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['image', 'caption', 'comments']