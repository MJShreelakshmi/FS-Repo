from django.urls import path
from fashion.views import *

urlpatterns = [
    path('jewellery/',jewellery, name = 'jewelleries'),
    path('outfits/',outfits, name = 'outfits')
]