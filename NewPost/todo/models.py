from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=250)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    user = models.ForeignKey(get_user_model(),related_name='Пользователь',on_delete=models.CASCADE)


    def __str__(self):
        return self.title




class User(models.Model):
	email = models.EmailField(verbose_name="email", max_length=60, unique=True)
	username = models.CharField(max_length=30, unique=True)
	password = models.CharField(max_length=30)
user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,null=True)
