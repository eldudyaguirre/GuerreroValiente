from django.contrib import admin
from .models import Publicacion, Video


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "categoria",
        "publicado",
        "fecha_publicacion",
    )
    list_filter = ("publicado", "categoria")
    search_fields = ("titulo", "resumen", "contenido")
    prepopulated_fields = {"slug": ("titulo",)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "publicado", "fecha_creacion")
    list_filter = ("publicado",)
    search_fields = ("titulo", "descripcion")