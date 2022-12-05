from django import forms


class Registr_form(forms.Form):
    Name = forms.CharField(label='User Name' ,widget=forms.TextInput(
        attrs={}
    ))

    Password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={}
    ))

    Email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={}
    ))


class Login(forms.Form):
    Password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={}
    ))

    Name = forms.CharField(label='User Name' ,widget=forms.TextInput(
        attrs={}
    ))