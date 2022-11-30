from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError(_('Phone field must be set'))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = PhoneNumberField(_("Phone Number"), region="KZ", unique=True, db_index=True)
    password = models.CharField(_("Password"), max_length=256)
    birth_date = models.DateField(_("Birth Date"), null=True, blank=True)
    is_staff = models.BooleanField(_("Admin"), default=False)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELD = ["password"]

    def __str__(self):
        return str(self.phone)

    objects = CustomUserManager()

    @property
    def role(self):
        if self.admin:
            return "admin"
        elif self.doctor:
            return "doctor"
        elif self.patient:
            return "patient"
        return None

    class Meta:
        db_table = "users"
        verbose_name = _("User")
        verbose_name_plural = _("Users")
