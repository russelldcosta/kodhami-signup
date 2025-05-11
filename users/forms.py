from django import forms
from django.core.validators import RegexValidator
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='First name can only contain alphabets.'
            )
        ]
    )
    last_name = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='Last name can only contain alphabets.'
            )
        ]
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$&!])[A-Za-z\d@#$&!]{6,}$',
                message='Password must have at least 6 characters, one letter, one number, and one of @#$&!'
            )
        ]
    )
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password != repeat_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user