from django.db import models
import os
import uuid
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from .fields import WEBPField
from django.contrib.auth.models import AbstractUser

fractions =(('T','Terran'), ('P','Protoss'), ('Z','Zerg'))
def image_folder(instance, filename):
    return 'units/static/dist/img/UnitModel/{}.webp'.format(uuid.uuid4().hex)
def image_folder_bck(instance, filename):
    return 'units/static/dist/img/UnitModel/bck/{}.webp'.format(uuid.uuid4().hex)

def image_folder_avatar(instance, filename):
    return 'units/static/dist/img/UnitModel/bck/{}.webp'.format(uuid.uuid4().hex)


# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, blank=True, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    img_bck = WEBPField(
        verbose_name=_('Avatar'),
        upload_to=image_folder_avatar,
        default='units/static/dist/img/no_image_big.png',
    )

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    def str(self):
        return self.email


class Unitsdb(models.Model):
    name = models.CharField('Наименование юнита',max_length=30, default='')
    fr = models.CharField('Фракция',max_length=1,choices=fractions, unique=False, null=False)
    type = models.CharField('Тип юнита',max_length=100, default='')
    short_des = models.TextField('Краткое описание', default='')
    des = models.TextField('Описание', default='', null=True)
    time_create = models.DateTimeField('Дата публикации', auto_now_add=True)
    time_update = models.DateTimeField('Дата изменении', auto_now=True)
    author = models.ForeignKey(CustomUser, verbose_name = 'Пользователь',  on_delete=models.CASCADE)
    img = WEBPField(
        verbose_name=_('ImageIcon'),
        upload_to=image_folder,
        default='units/static/dist/img/no_image_big.png',
    )
    img_bck = WEBPField(
        verbose_name=_('ImageBck'),
        upload_to=image_folder_bck,
        default='units/static/dist/img/no_image_big.png',
    )
    #settings.AUTH_USER_MODEL,

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/units/{self.id}'
    class Meta:
        verbose_name = "Юнит"
        verbose_name_plural = "Юниты"


