from django.forms import ModelForm, TextInput, PasswordInput

from Auth.models import UserInfo


class SignUpForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'password', 'telephone' ,'email']
        labels = {
            'username': 'username',
            'password': 'password',
            'telephone': 'telephone',
            'email': 'email'
        }

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'telephone': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
        }

class SignInForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'password']
        labels = {
            'username': 'username',
            'password': 'password'
        }

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'})
        }
