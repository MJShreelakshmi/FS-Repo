"""
URL configuration for conditional_statements project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from iff.views import *
from if_elif.views import *
from if_elif_else.views import *
from ffor.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jinja_if/', jinja_if, name = 'jinja_if'),
    path('if_elif/', if_elif, name = 'if_elif'),
    path('if_elif_else/',if_elif_else , name = 'if_elif_else'),
    path('jinja_for/', jinja_for, name = 'jinja_for'),
    
]
