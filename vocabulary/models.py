from django.db import models

# Create your models here.
class Level(models.Model):
    level = models.CharField(max_length=16)

    def __str__(self):
        return self.level

class Word(models.Model):
    word = models.CharField(max_length=128)
    ru1 = models.CharField(max_length=128, null=True)
    ru2 = models.CharField(max_length=128, null=True)
    
    level = models.ForeignKey(Level, null=True, on_delete=models.SET_NULL)

    picture = models.CharField(max_length=128, null=True)
    audio = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f"{self.word.upper()}:  {self.ru1} / {self.ru2}"