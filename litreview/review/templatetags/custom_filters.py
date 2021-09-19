from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def to_stars(value: int, max_: int = 5):
    html = f"<span class=filled-stars>{'★'*min(value, max_)}</span>"
    html += f"<span class=empty-stars>{'★'*(max_-value)}</span>"
    return mark_safe(html)
