from django import forms
from django.core.validators import RegexValidator
from .models import CustomUser

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'validate-input',
            'data-pattern': '^[a-zA-Z]+$',
            'data-error': 'Only alphabets allowed'
        }),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='First name can only contain alphabets.'
            )
        ]
    )
    
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'validate-input',
            'data-pattern': '^[a-zA-Z]+$',
            'data-error': 'Only alphabets allowed'
        }),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='Last name can only contain alphabets.'
            )
        ]
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'validate-input',
            'data-pattern': '^(?=.*[A-Za-z])(?=.*\\d)(?=.*[@#$&!])[A-Za-z\\d@#$&!]{6,}$',
            'data-error': 'Need 6+ chars with letter, number, and special character'
        }),
        validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$&!])[A-Za-z\d@#$&!]{6,}$',
                message='Password must have at least 6 characters, one letter, one number, and one of @#$&!'
            )
        ]
    )
    
    repeat_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'validate-input',
            'data-match': 'password',
            'data-error': 'Passwords must match'
        })
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'validate-input',
                'data-pattern': '^[\\w.%+-]+@[\\w.-]+\\.[a-zA-Z]{2,}$',
                'data-error': 'Invalid email format'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'validate-input',
                'data-pattern': '^(\\+[1-9]\\d{12}|[1-9]\\d{9})$',
                'data-error': 'Invalid phone format'
            })
        }

    def clean(self):

        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password and repeat_password and password != repeat_password:
            self.add_error('repeat_password', "Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email