from django.urls import path
from .views import home

app_name = 'foxes'
urlpatterns = [
    path('', home, name='index'),
]