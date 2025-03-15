"""
URL configuration for password_manager project.

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
from codecs import namereplace_errors

from django.contrib import admin
from django.urls import path, include
from password import views
from password.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name="home"),
    path('logout/', views.logout_page, name="logout"),
    path('buttons/', views.overview, name="buttons"),
    path('passwordgenerator/', Index.as_view(), name="index"),
    path('passwordmanager/', views.password_manager, name="passwordmanager"),
    path('account/', include('account.urls'))
]
