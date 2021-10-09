from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

from .models import Profile

# Добавляем дополнительные поля пользователя
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user',
                    'phone_number',
                    'city',
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
                    'knee_girth'
                    )