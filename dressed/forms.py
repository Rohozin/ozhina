from django import forms
from django.contrib.auth.models import User
from .models import Profile, Order

# Добавляем дополнительные поля пользователя
class LoginForm(forms.Form):
    username    = forms.CharField()
    password    = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password    = forms.CharField(label='Введіть пароль', widget=forms.PasswordInput)
    password2   = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput)
    
    class Meta:
        model   = User
        fields  = (
                    'username', 
                    'first_name', 
                    'email'
                    )
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model   = User
        fields  = (
                    'first_name',
                    'email'
                    )

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model   = Profile
        fields  = (
                    'city',
                    'hair',
                    'full_height',
                    'neck_girth',
                    'chest_girth',
                    'chest_height',
                    'center_chest',
                    'back_width',
                    'shoulder_long',
                    'long_sleeves',
                    'arm_girth',
                    'wrist_girth',
                    'waist_circumference',
                    'length_front_waist',
                    'long_back_waist',
                    'long_waist_knee',
                    'hip_girth',
                    'thigh_girth',
                    'knee_girth')

class OrderEditForm(forms.ModelForm):
    class Meta:
        model   = Order
        fields  = ( 
                    'name',
                    'phone_number',
                    'massege', 
                    'image',
                    'cat', 
                    )
    