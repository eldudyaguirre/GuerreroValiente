from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    resumen = models.CharField(max_length=300, blank=True)
    contenido = models.TextField()
    imagen = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True,
    )
    categoria = models.CharField(max_length=100, blank=True)
    publicado = models.BooleanField(default=False)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_publicacion"]
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.titulo)[:200] or "publicacion"
            candidato = base
            numero = 2

            while Publicacion.objects.filter(
                slug=candidato
            ).exclude(pk=self.pk).exists():
                candidato = f"{base}-{numero}"
                numero += 1

            self.slug = candidato

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo


class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    url = models.URLField(max_length=500)
    miniatura = models.URLField(max_length=500, blank=True)
    publicado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "Video"
        verbose_name_plural = "Videos"

    def __str__(self):
        return self.titulo