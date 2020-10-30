from django.contrib import admin
from .models import Word, Level, WordWordset, UserWordset

# Register your models here.
# admin.site.register(Word)
admin.site.register(Level)

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    model = Word

class WordWordsetInline(admin.TabularInline):
    model = WordWordset
    list_display = ['id', 'word', 'stage']
    extra = 1

@admin.register(UserWordset)
class UserWordset(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'get_words_str']
    inlines = (WordWordsetInline,)

    