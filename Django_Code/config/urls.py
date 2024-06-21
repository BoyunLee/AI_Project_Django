"""
URL configuration for config project.

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
from django.urls import path, include
from mainapp import views as m_views

urlpatterns = [
    path('front/', include('frontapp.urls')),
    path('visualization/',m_views.visualization),
    path('',m_views.login),
    path('login/',m_views.gologin),
    path('outline/',m_views.outline),
    path('predict/',m_views.predict),
    path('predict/predict_update/',m_views.predict_View),
    path('team/',m_views.team),
]
