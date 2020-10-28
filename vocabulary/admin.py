from django.contrib import admin
from .models import Word, Level

# Register your models here.
# admin.site.register(Word)
admin.site.register(Level)

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    model = Word