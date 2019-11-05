from django import template
register = template.Library()

from forms.models import Post

@register.simple_tag(name='simple')
def any_function():
    return Post.objects.count()

@register.filter(name='total_count')
def count(value):
    return 'ok' if value>10 else 'too low'

@register.inclusion_tag('results.html')
def posts_list():
    posts = Post.objects.all()
    return {'posts':posts}

