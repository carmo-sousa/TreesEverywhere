from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput,
        max_length=64,
        required=True,
    )
