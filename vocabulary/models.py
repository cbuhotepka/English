from django.db import models
from django.conf import settings

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    word = models.ManyToManyField(Word, through='WordVocabulary')
    
    class Meta:
        verbose_name_plural = 'UserVocabularies'

    def __str__(self):
        return f"{self.title} ({self.user.username})"

    def get_words_str(self):
        words = self.word.all()[:6].values_list('word', flat=True)
        if len(words) == 6:
            return ', '.join(words[:5])+'...'
        else:
            return ', '.join(words)
    get_words_str.short_description = 'Words'

class WordVocabulary(models.Model):
    vocabulary = models.ForeignKey(UserVocabulary, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    stage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.word.word} - {self.stage}"