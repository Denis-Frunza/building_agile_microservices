from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from user_auth.enums import GenderChoices, StatusChoices

class AbstractBaseUser(AbstractUser):
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    created_by = models.IntegerField(null=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    updated_by = models.IntegerField(null=True)

    is_deleted = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(default=None, null=True)
    deleted_by = models.IntegerField(null=True)
    

    objects = UserManager()
    class Meta: 
        abstract = True


class User(AbstractBaseUser):
    first_name = models.CharField(
        max_length=100, null=True, verbose_name='First Name', help_text='First name of  user')
    last_name = models.CharField(
        max_length=100, null=True, verbose_name='Last Name', help_text='Last name of  user')
    email = models.EmailField(
        max_length=100, unique=True,verbose_name='User email', help_text='Email of  user')
    phone_number = models.CharField(
        max_length=50, unique=False, null=True, verbose_name='Phone user', help_text='Phone of user')
    gender_choice = models.CharField(
        max_length=1, choices=GenderChoices.choices(), null=True, verbose_name='User sex', help_text='Sex of User')
    bvn = models.CharField(max_length=100, null=True, verbose_name='BVN', help_text='Bank Verification Number')
    birthday = models.DateField(null=True, verbose_name='Birthday', help_text='Birthday of user')
    status = models.CharField(
        max_length=100,
        choices=StatusChoices.choices(),
        default=StatusChoices.ACTIVE.value,
        verbose_name='User status',
        help_text='User status'
    )
    last_login = models.DateTimeField(
        verbose_name='Last login', help_text='Last login', auto_now_add=True)

    class Meta:
        """Metadata"""
        ordering = ["first_name", "last_name"]

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
