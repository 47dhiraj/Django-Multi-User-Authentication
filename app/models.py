from django.db import models

from django.contrib.auth.models import Permission
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=True)

		