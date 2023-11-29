"""
URL configuration for project18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bootstrap2/',bootstrap2,name='bootstrap2'),
    path('bootstrap2_cdn/',bootstrap2_cdn,name='bootstrap2_cdn'),
    path('bootstrap/',bootstrap,name='bootstrap'),
    path('madhan1/',madhan1,name='madhan1'),
    path('badges/',badges,name='badges'),
    path('button_group/',button_group,name='button_group'),
]
