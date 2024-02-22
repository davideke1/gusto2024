# your_app/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='add_class_and_attributes')
def add_class_and_attributes(value, css_class_and_attributes):
    attrs = value.field.widget.attrs
    for part in css_class_and_attributes.split('|'):
        if '=' in part:
            attr, val = part.split('=')
            attrs[attr.strip()] = val.strip()
        else:
            attrs['class'] = f"{attrs.get('class', '')} {part.strip()}"

    return value
