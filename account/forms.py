from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
         widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    #This method is called when we validate the form calling its is_valid() method.
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']



class LoginForm(forms.Form):
    username = forms.CharField()

    # Uses the PasswordInput widget to render its HTML input element,
    # including a type="password" attribute
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    """
        Will allow users to edit their data fields stored in the
        built-in User model.
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    """
        Will allow users to edit their extra data saved in the
        custom Profile model.
    """
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

