from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter
def remove_hashtag(string):
    string = string.replace("#", "%23")
    return string