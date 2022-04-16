from django.urls import path
from main.views import first

urlpatterns = [
    path('', first, name='index'),
]
