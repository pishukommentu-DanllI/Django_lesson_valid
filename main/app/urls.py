from django.urls import path, include
from .views import *

urlpatterns = [
    path('registr', registr, name='registr'),
    path('weclom', weclom, name='welcome'),
    path('login', login, name='login')
]