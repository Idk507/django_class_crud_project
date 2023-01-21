from django import template
from .models import student
register = template.Library()

@register.simple_tag()
def custlower(value):
    result = value[:3].lower()
    return result

register.filter("mylower",custlower)

@register.filter(name="append")
def custappend(value,arg):
    result=str(arg)+value
    return result
    
