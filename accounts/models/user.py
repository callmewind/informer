from django.contrib.auth.models import BaseUserManager, AbstractUser as DjangoUser
from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils.translation import gettext_lazy as _
from .account import Account

class UserManager(BaseUserManager):
    def _create_user(self, email, first_name, account, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = User(email=email, first_name=first_name, account_id=account, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, account, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, first_name, account, password, **extra_fields)

    def create_superuser(self, email, first_name, account, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, first_name, account, password, **extra_fields)


class User(DjangoUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'first_name', 'account' ]
    
    objects = UserManager()

    username = None
    email = models.EmailField(_("email address"), unique=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=_('account'), related_name='users')
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)