from django.db import models
from django.db import models
import os
import uuid
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class PHdb(models.Model):
    name = models.CharField('пользователь',max_length=30, default='')
    pn = models.CharField('телефон', max_length=30, default='', unique=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"