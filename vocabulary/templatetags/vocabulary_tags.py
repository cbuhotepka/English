from django import template
from vocabulary.models import Level, UserVocabulary

register = template.Library()

@register.simple_tag()
def all_levels():
    return Level.objects.all()

@register.simple_tag()
def user_vocabulary_set(user):
    return UserVocabulary.objects.filter(user=user)