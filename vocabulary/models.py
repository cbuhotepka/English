from django.db import models
from django.contrib.auth import User

# Create your models here.
class Level(models.Model):
    level = models.CharField(max_length=16)

    def __str__(self):
        return self.level

class Word(models.Model):
    word = models.CharField(max_length=128)
    ru1 = models.CharField(max_length=128, blank=True)
    ru2 = models.CharField(max_length=128, blank=True)
    
    level = models.ForeignKey(Level, null=True, on_delete=models.SET_NULL)

    picture = models.CharField(max_length=128, blank=True)
    audio = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f"{self.word.upper()}:  {self.ru1} / {self.ru2}"

class UserVocabulary(models.Model):
    pass
