from django import template
from vocabulary.models import Level, UserWordset

register = template.Library()

@register.simple_tag()
def all_levels():
    return Level.objects.all()

@register.simple_tag()
def user_wordset_list(user):
    return UserWordset.objects.filter(user=user)