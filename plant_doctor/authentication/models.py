from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import TimestampMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The given Email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
    
    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password
        )
        
        user.is_staff = True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser, PermissionsMixin, TimestampMixin):
    first_name = models.CharField(_("First Name"), max_length=50, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True, null=True)
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False, help_text=_("Determines whether this user can login to the admin page."))
    is_active = models.BooleanField(_("Active"), help_text=_("Designates whether the user can login to the system."), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self) -> str:
        return str(self.first_name) + str(self.last_name)