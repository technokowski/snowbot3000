"""snowbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mainapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index'),
    url(r'^support/', views.support,name='support'),
    url(r'^text_input/$', views.text_input, name='text_input'),
    url(r'^jokes/$', views.jokes, name='jokes'),
    url(r'^songs/$', views.songs, name='songs'),
    url(r'^wisdom/$', views.wisdom, name='wisdom'),
    url(r'^dareyou/$', views.dareyou, name='dareyou'),
    url(r'^voice/$', views.voice, name='voice'),
    url(r'^support_input/$', views.support_input, name='support_input'),
]
