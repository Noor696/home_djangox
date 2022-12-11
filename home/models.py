from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


class Home(models.Model):

    img_url = models.TextField(default="no image provided")
    rooms = models.IntegerField()
    description = models.TextField(default="🏡")
    owner = models.ForeignKey(CustomUser , on_delete=models.CASCADE) 
    position = models.CharField(max_length=64)


   
    def __str__(self):
        return self.name

    class Meta:
       ordering = ["-pk"] 

    def get_absolute_url(self):  
        return reverse("home_detail", args={self.id})
    
