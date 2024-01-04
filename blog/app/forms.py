from django import forms
from app.models import Comments,Subscribe
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields = {'content','name','email','website'}
        
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'Type your comment....'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['website'].widget.attrs['placeholder'] = 'Website'
        
        
class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe      
        fields='__all__'  
        labels={
            'email':_('')
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your Email'
        
        
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","password1","password2")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter Password again'    
    
    def clean_username(self):
        username=self.cleaned_data['username'].lower()
        new=User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError("User already exist")
        else:
            return username    
        
    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        new=User.objects.filter(email=email)
        if new.count():
            raise forms.ValidationError("Email already exist")
        else:
            return email     
        
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2