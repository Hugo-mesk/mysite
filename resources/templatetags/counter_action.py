from django import template
register = template.Library()

@register.simple_tag
def counter(val=None):
    if val == "":
        return 0
    else:
        return val + 1
