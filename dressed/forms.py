from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

from .models import Profile

# Добавляем дополнительные поля пользователя
class SignUpForm (UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='A valid email address, please.')
    day = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'day', 'password1', 'password2')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number',
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