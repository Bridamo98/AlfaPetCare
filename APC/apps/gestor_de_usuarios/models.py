from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

class Topico(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)
    def __str__(self): #To string
        return self.nombre

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tfno = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1000000),MaxValueValidator(9999999999)])
    topicos = models.ManyToManyField(Topico, blank=True)
    #profile_img=models.ImageField(upload_to='images/profile/',default='images/profile/perfilb.jpg',null=False,blank=False)
    def __str__(self): #To string
        return self.user.username
