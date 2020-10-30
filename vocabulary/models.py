from django.db import models
from django.conf import settings

# Create your models here.
class Level(models.Model):
    level = models.CharField(max_length=16)

    def __str__(self):
        return self.level

class Word(models.Model):
    eng = models.CharField(max_length=128)
    ru1 = models.CharField(max_length=128, blank=True)
    ru2 = models.CharField(max_length=128, blank=True)
    
    level = models.ForeignKey(Level, null=True, on_delete=models.SET_NULL)

    picture = models.CharField(max_length=128, blank=True)
    audio = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f"{self.eng.upper()}:  {self.ru1} / {self.ru2}"

class UserWordset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    words = models.ManyToManyField(Word, through='WordWordset')
    picture = models.CharField(max_length=128, default='__blank__.jpg')
    
    class Meta:
        verbose_name_plural = 'UserVocabularies'

    def __str__(self):
        return f"{self.title} ({self.user.username})"

    def get_words_str(self):
        words = [w.eng for w in self.words.all()[:6]]
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

class WordWordset(models.Model):
    wordset = models.ForeignKey(UserWordset, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    stage = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('wordset', 'word')

    def __str__(self):
        return f"{self.word.eng} - {self.stage}"