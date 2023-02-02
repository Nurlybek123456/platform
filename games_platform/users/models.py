from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from core.models import CommonModel

from .choices import all_roles_choices


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, role="GAMER"):
        if not email:
            raise ValueError("Users must have email address")
        if not username:
            raise ValueError("Users must have username")
        if not password:
            raise ValueError("Users must have password")
        if not role:
            raise ValueError("Users must have role")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, CommonModel):
    email = models.EmailField(
        verbose_name="email",
        max_length=100,
        unique=True,
    )
    username = models.CharField(
        verbose_name="username",
        max_length=255,
        unique=True,
    )
    role = models.CharField(
        verbose_name="role",
        max_length=30,
        choices=all_roles_choices,
    )
    last_login = models.DateTimeField(
        verbose_name="last_login",
        null=True,
        blank=True,
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()
    def __srt__(self):
        return self.username + ',' + self.email


# class UserDetail(CommonModel):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE
#     )
