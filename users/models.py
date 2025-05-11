from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r'^(\+[1-9]\d{12}|[1-9]\d{9})$',
                message="Phone number must be in the format: '+1234567890123' or '1234567890' without leading 0."
            )
        ]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.email
