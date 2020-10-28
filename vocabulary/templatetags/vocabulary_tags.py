from django import template
from vocabulary.models import Level

register = template.Library()

@register.simple_tag()
def all_levels():
    return Level.objects.all()