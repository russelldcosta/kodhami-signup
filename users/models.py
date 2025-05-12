from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.auth.base_user import BaseUserManager

# how users are created
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# actual user definition
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

    objects = CustomUserManager()

    def __str__(self):
        return self.email





