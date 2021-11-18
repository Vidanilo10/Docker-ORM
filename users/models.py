from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser

class UserProfileManager(BaseUserManager):

    def create_user(self, email, name, password):
        if not email:
            raise ValueError('The user needs a email.')

        user = self.model(
            email=self.normalize_email(email), 
            name=name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email, 
            name, 
            password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self) -> str:
        return self.name
    
    def get_short_name(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.email
