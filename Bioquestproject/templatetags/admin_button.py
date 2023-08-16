from django import template

register = template.Library()

@register.simple_tag
def admin_button(user):
    if user.is_authenticated and user.is_superuser:
        return '<button>Admin Button</button>'
    return ''
