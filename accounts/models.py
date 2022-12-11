from django.contrib.auth.models import AbstractUser
from django.db import models

# CustomUser fields inheret from AbstractUser class 
class CustomUser(AbstractUser):
    # i can add any filed i want

    phone_number = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.email