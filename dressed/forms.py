from django import forms
from django.contrib.auth.models import User
from .models import Course, Profile, Order, Category, OrderTeach


class LoginForm(forms.Form):
    username    = forms.CharField(label='You username')
    password    = forms.CharField(label='You password')

    class Meta:
        model   = User
        fields  = (
                    'username', 
                    'password ', 
                )
        widgets = {
                    'username': forms.TextInput(attrs={'class': 'form-input'}),
                    'password ': forms.TextInput(attrs={'class': 'form-input'}),
                }

class UserRegistrationForm(forms.ModelForm):
    password    = forms.CharField(label='Enter the password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2   = forms.CharField(label='Repeat the password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model   = User
        fields  = (
                    'username', 
                    'first_name', 
                    'email',
                )
        widgets = {
                    'username': forms.TextInput(attrs={'class': 'form-input'}),
                    'first_name': forms.TextInput(attrs={'class': 'form-input'}),
                    'email': forms.TextInput(attrs={'class': 'form-input'}),
                }
    
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
        widgets = {
                    'first_name': forms.TextInput(attrs={'class': 'form-input'}),
                    'email' : forms.TextInput(attrs={'class': 'form-input'}),
                }  

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model   = Profile
        fields  = (
                    'phone',
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
        widgets = {
                    'phone': forms.TextInput(attrs={'class': 'form-input'}),
                    'full_height': forms.TextInput(attrs={'class': 'form-input'}),
                    'neck_girth' : forms.TextInput(attrs={'class': 'form-input'}),
                    'chest_girth' : forms.TextInput(attrs={'class': 'form-input'}),
                    'chest_height' : forms.TextInput(attrs={'class': 'form-input'}),
                    'center_chest' : forms.TextInput(attrs={'class': 'form-input'}),
                    'back_width' : forms.TextInput(attrs={'class': 'form-input'}),
                    'shoulder_long' : forms.TextInput(attrs={'class': 'form-input'}),
                    'long_sleeves' : forms.TextInput(attrs={'class': 'form-input'}),
                    'arm_girth' : forms.TextInput(attrs={'class': 'form-input'}),
                    'wrist_girth': forms.TextInput(attrs={'class': 'form-input'}),
                    'waist_circumference' : forms.TextInput(attrs={'class': 'form-input'}),
                    'length_front_waist' : forms.TextInput(attrs={'class': 'form-input'}),
                    'long_back_waist' : forms.TextInput(attrs={'class': 'form-input'}),
                    'long_waist_knee' : forms.TextInput(attrs={'class': 'form-input'}),
                    'hip_girth': forms.TextInput(attrs={'class': 'form-input'}),
                    'thigh_girth' : forms.TextInput(attrs={'class': 'form-input'}),
                    'knee_girth' : forms.TextInput(attrs={'class': 'form-input'}),
                }    

class OrderEditForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Select a category',widget=forms.Select(attrs={'class': 'form-inputtwo'}))
    
    class Meta:
        model   = Order
        fields  = ( 
                    'name',
                    'phone_number',
                    'massege', 
                    'image',
                    'cat',
                    'agreement', 
                )
        widgets = {
                    'name': forms.TextInput(attrs={'class': 'form-input'}),
                    'massege' : forms.Textarea(attrs={'cols': 35, 'rows': 5, 'class': 'form-input'}),
                    'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
                    'image': forms.FileInput(attrs={'class': 'form-inputon'}),
                }      

class OrderFormTeach(forms.ModelForm):

    course = forms.ModelChoiceField(queryset=Course.objects.all(),empty_label='Select a category',widget=forms.Select(attrs={'class': 'form-inputtwoteach'}))
    
    class Meta:
        model   = OrderTeach
        fields  = (
                    'name',
                    'phone_number',
                    'massege',
                    'course',
                    'agreement',
                )
        widgets = {
                    'name': forms.TextInput(attrs={'class': 'form-inputteach'}),
                    'phone_number': forms.TextInput(attrs={'class': 'form-inputteach'}),
                    'massege' : forms.Textarea(attrs={'cols': 35, 'rows': 5, 'class': 'form-inputteach'}),
                }