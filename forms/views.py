from django.shortcuts import render

from .models import *
def hello(request):

    template_name = 'register_tag.html'
    value = Post.objects.count()

    return render(request,template_name,{'value':value})

