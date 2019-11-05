from django.urls import path
from .views import hello

urlpatterns = [
    path('register/', hello, name='hi')
]