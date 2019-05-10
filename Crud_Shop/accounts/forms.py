from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model)

User = get_user_model()

#This section lays out how the front end form will react. It takes in the username and passwords for registrationa and login
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('passwrd')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            elif not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            elif not user.is_active:
                raise forms.ValidationError('User not active!')
            return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]
