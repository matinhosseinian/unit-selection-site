from django import template

register = template.Library()

@register.filter(name='dict_key')
def dict_key(d, key):
    if d[key]:
        return d[key]
    else:
        return ""