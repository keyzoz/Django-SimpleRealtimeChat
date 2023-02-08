from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000,verbose_name='Название чата')
  
class Message(models.Model):
    value = models.CharField(max_length=1000,null=True,verbose_name='Текст сообщения')
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000,null=True)