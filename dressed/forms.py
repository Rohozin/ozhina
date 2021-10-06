from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime

# Добавляем дополнительные поля пользователя
class SignUpForm (UserCreationForm):
    first_name = forms.CharField(initial='Your name',max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='A valid email address, please.')
    phone_number = forms.CharField(max_length=20)
    day = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = User
        fields = ('first_name', 'email', 'username', 'day', 'password1', 'password2')