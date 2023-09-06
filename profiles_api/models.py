from django.db import models
""" These are the standard base classes you need to use
when overiding or customzing the default django user model"""
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normailize_email(email)
        """Create user model"""
        user = self.model(email=email,name=name)

        user.set_password(password)
        """Savin the user model"""
        user.save(using=self._db)

        return users

    def create_superuser(self,email,name,password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=225,unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    """Next we Specify the model manager that we are going to
       use for the objects and this is required because we need
       to use our custom user model with the Django CLI, so django
        needs to have a custom model manager fot the user models
        so it knows how to create users and control users using the django
        Command line tools."""

    objects = UserProfileManager()

    """Below this we need to add a couple of more fields to our class
        and this is for it to work with the Django admin and also the
        Django authentication system"""

    """We need to Specify a username field and this is because we're overriding
        the default username field which is normally called username and we're
        replacing it with our email field"""

    """So this means when we authenticate , instead of them providing a username
    and password they're just going to provide their email address and password"""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string represenation of our user"""
        return self.email



"""Now that we have our Custom user model we can go ahead and create a manager
    so that Django knows how tot work with this custom user model in the Django
    command-line tools """


"""EASY WAY:Now because we have customized our user model we need to tell django
    how to interact with this user model in order to create users because by default when
    it creates a user it expexts a username and a password field but we've replaced
    username field with email field so we just need to create a custom manager that
    can handle creating users with an email field instead of a username field
    We are going to create custom model manager class just above UserProfile class"""
