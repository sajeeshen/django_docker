from django.contrib.auth.models import ( AbstractBaseUser,
                                          BaseUserManager,
                                          PermissionsMixin  
                                        )
from django.db import models
USER_TYPE = (
    ('ADMIN', 'ADMIN'),
    ('USER', 'USER'),
    ('ARTIST', 'ARTIST')
)


class UserManager(BaseUserManager):
    """ Manager class for Users """
    
    def create_user(self, email, password, **extra_fields):
        """ Function for creating users """
        # Checking email is not null
        if not email:
            raise ValueError('User must have a valid email')
        user = self.model(email=self.normalize_email(email),
                            **extra_fields)
        # Set the passwordk
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """ Custom function for creating super user """

        user = self.create_user(email, password, **extra_fields)
        user.user_type='ADMIN'
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model """

    email = models.EmailField(unique=True, max_length=250)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=200)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField('User Type',max_length=20,
                                    choices=USER_TYPE, default='USER')

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name+" "+self.last_name
