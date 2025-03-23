from django.forms import ModelForm, TextInput, PasswordInput, CharField

from authentication.models import UserInfo


class SignUpForm(ModelForm):
    confirm_password = CharField(
        label='confirm password',
        widget=PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
    )

    class Meta:
        model = UserInfo
        fields = ['username', 'password', 'confirm_password', 'telephone', 'email']
        labels = {
            'username': 'username',
            'password': 'password',
            'confirm_password': 'confirm_password',
            'telephone': 'telephone',
            'email': 'email'
        }

        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': PasswordInput(attrs={'class': 'form-control'}),
            'confirm_password': PasswordInput(attrs={'class': 'form-control'}),
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
