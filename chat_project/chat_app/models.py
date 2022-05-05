from django.db import models
from django.urls import reverse

# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=128, verbose_name='название')

    def get_absolute_url(self):
        return f'/chat/{self.name}/'