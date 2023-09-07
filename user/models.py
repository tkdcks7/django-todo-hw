from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile = models.TextField(null=True, blank=True)