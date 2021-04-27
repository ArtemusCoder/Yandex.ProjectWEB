from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label=(u'Имя пользователя'))
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50, label=(u'Фамилия'), required=True, widget=forms.TextInput(attrs={'placeholder': ('Фамилия')}))
    last_name= forms.CharField(max_length=50, required=True, label=(u'Имя'), widget=forms.TextInput(attrs={'placeholder': ('Имя')}))
    password1 = forms.CharField(label=(u'Пароль'), widget=forms.PasswordInput())
    password2 = forms.CharField(label=(u'Пароль еще раз'), widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']
    


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField(label=(u'Имя пользователя'))
    first_name = forms.CharField(max_length=50, label=(u'Фамилия'), required=True, widget=forms.TextInput(attrs={'placeholder': ('Фамилия')}))
    last_name= forms.CharField(max_length=50, required=True, label=(u'Имя'), widget=forms.TextInput(attrs={'placeholder': ('Имя')}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        exclude = ['user']


class LoginForm(forms.ModelForm):
    username = forms.CharField(label=(u'Имя пользователя'))
    password = forms.CharField(label=(u'Пароль'))

    class Meta:
        model = User
        fields = ('username', 'password')


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label=(u'Имя пользователя'))
    password = forms.CharField(label=(u"Пароль"), widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'Вы вели данные неправильно'
        super().__init__(*args, **kwargs)