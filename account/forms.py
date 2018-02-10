from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()

    # Uses the PasswordInput widget to render its HTML input element,
    # including a type="password" attribute
    password = forms.CharField(widget=forms.PasswordInput)

