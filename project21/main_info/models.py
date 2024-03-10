from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


# my usermanager
class MyUserManager(BaseUserManager):

    def creat_user(self, email, username, password):
        if not email or not username or not password:
            raise ValueError("one of the fields was missing")
        user = self.model(
            email = self.normalize_email(email), 
            username = username
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password):
        if not email or not username or not password:
            raise ValueError("one of the fields was missing")
        user = self.model(
            email = self.normalize_email(email), 
        )
        user.username = username
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user



class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=30, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(null=True, blank=True)
    password = models.CharField(max_length=150, blank=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["password",]

    objects = MyUserManager()

    def __str__(self) -> str:
        return self.username
    
    def get_full_name(self):
        '''
        Returns the User name.
        '''
        return self.user_name


# am to revisit this while setting up the email verification functionality
"""
    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
"""