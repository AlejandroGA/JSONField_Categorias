#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db import models

class Servicios(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Belleza(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Clases(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Fiestas(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Hogar(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Mantenimiento(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Mascotas(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Otros(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Profesionales(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Recreacion(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()

class Reparacion(models.Model):
    foto1 = models.ImageField(upload_to='img/servicio')
    foto2 = models.ImageField(upload_to='img/servicio')
    foto3 = models.ImageField(upload_to='img/servicio')
    foto4 = models.ImageField(upload_to='img/servicio')
    foto5 = models.ImageField(upload_to='img/servicio')
    titulo = models.CharField(max_length=100)
    datos = JSONField()





