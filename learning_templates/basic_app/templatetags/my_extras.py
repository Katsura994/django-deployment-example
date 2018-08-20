from django import template

register = template.Library()

@register.filter(name='cut12')
def cut(value,arg):
    """
        This cuts out all values of arg from the string
    """
    return value.replace(arg,'')

# register.filter('cut12',cut)
