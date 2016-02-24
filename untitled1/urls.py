"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'inmuebles.views.servicios', name='servicios'),
    url(r'^belleza/', 'inmuebles.views.belleza', name='belleza'),
    url(r'^clases/', 'inmuebles.views.clases', name='clases'),
    url(r'^fiestas/', 'inmuebles.views.hogar', name='hogar'),
    url(r'^mantenimiento/', 'inmuebles.views.mantenimiento', name='mantenimiento'),
    url(r'^mascotas/', 'inmuebles.views.mascotas', name='mascotas'),
    url(r'^otros/', 'inmuebles.views.otros', name='otros'),
    url(r'^profesionales/', 'inmuebles.views.profesionales', name='profesionales'),
    url(r'^reparacion/', 'inmuebles.views.reparacion', name='reparacion'),
    url(r'^recreacion/', 'inmuebles.views.recreacion', name='recreacion'),

]
