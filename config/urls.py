from django.contrib import admin
from django.urls import path

from contenido import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("acerca/", views.acerca, name="acerca"),
    path("blog/", views.blog, name="blog"),
    path("blog/<slug:slug>/", views.detalle_publicacion, name="detalle_publicacion"),
    path("recursos/", views.recursos, name="recursos"),
    path("videos/", views.videos, name="videos"),
    path("literatura/", views.literatura, name="literatura"),
    path("naranon/", views.naranon, name="naranon"),
    path("contactos/", views.contactos, name="contactos"),
]
