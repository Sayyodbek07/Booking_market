from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Username majburiy")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
