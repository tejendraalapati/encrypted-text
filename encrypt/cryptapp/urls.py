# cryptoapp/urls.py
from django.urls import path
from .views import home, encrypt, decrypt

urlpatterns = [
    path('', home, name='home'),
    path('encrypt/', encrypt, name='encrypt'),
    path('decrypt/', decrypt, name='decrypt'),
]
