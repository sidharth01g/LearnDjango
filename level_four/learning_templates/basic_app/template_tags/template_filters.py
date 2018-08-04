from django import template

register = template.Library()


@register.filter(name='cut')
def cut(string_: str, substring: str) -> str:
    return string_.replace(substring, '')
