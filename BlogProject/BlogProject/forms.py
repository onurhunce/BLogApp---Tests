from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = User.objects.create_user(self.cleaned_data[
            'username'], self.cleaned_data['email'], self.cleaned_data['password1'])

        return user
