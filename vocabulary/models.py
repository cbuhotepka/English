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
    picture = models.CharField(max_length=128, default='__blank__.jpg')
    
    class Meta:
        verbose_name_plural = 'UserVocabularies'

    def __str__(self):
        return f"{self.title} ({self.user.username})"

    def get_words_str(self):
        words = [w.word for w in self.word.all()[:6]]
        # words = Word.objects.all()[:5]
        print('>>> WORDS:', words)
        if words and len(words)>0 :
            # words = words.values_list('word', flat=True)
            if len(words) == 6:
                return ', '.join(words[:5])+'...'
            else:
                return ', '.join(words)
        else:
            return ''
    get_words_str.short_description = 'Words'

class WordVocabulary(models.Model):
    vocabulary = models.ForeignKey(UserVocabulary, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    stage = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('vocabulary', 'word')

    def __str__(self):
        return f"{self.word.word} - {self.stage}"