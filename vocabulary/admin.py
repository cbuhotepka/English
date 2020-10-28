from django.contrib import admin
from .models import Word, Level, WordVocabulary, UserVocabulary

# Register your models here.
# admin.site.register(Word)
admin.site.register(Level)

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    model = Word

class WordVocabularyInline(admin.TabularInline):
    model = WordVocabulary
    list_display = ['id', 'word', 'stage']
    extra = 1

@admin.register(UserVocabulary)
class UserVocabulary(admin.ModelAdmin):
    inlines = (WordVocabularyInline,)