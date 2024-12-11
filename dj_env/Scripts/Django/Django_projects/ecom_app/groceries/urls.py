from django.urls import path
from groceries.views import *

urlpatterns = [
    path('staple/', staple, name = 'staple'),
    path('spices/', spices, name = 'spices'),
]