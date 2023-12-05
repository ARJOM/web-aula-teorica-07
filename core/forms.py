from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        form = forms.ModelForm
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Login',
            'email': 'Email',
            'password': 'Password',
        }
