from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    #Manager para perfiles de usuario

    def create_user(self, email, name, password=None):
        #Crear nuevo user profile

        if not email:
            raise ValueError('Usuario debe tener un Email')
        
        email = self.normalize_email(email)

        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    #Modelo Base de datos para Usuarios en el Sistema
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        #obtener nombre completo
        return self.name

    def get_short_name(self):
        #obtener nombre corto del usuario
        return self.name

    def __str__(self):
        #retornar cadena representando nuestro usuario
        return self.email