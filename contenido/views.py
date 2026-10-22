from urllib.parse import urlparse, parse_qs
import re

from django.shortcuts import get_object_or_404, render

from .models import Publicacion, Video


def _youtube_embed(url):
    """Convierte enlaces comunes de YouTube a una URL de inserción segura."""
    if not url:
        return ""

    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    video_id = ""

    if host in {"youtu.be", "www.youtu.be"}:
        video_id = parsed.path.strip("/").split("/")[0]
    elif host.endswith("youtube.com") or host.endswith("youtube-nocookie.com"):
        if parsed.path == "/watch":
            video_id = parse_qs(parsed.query).get("v", [""])[0]
        else:
            match = re.match(r"^/(?:embed|shorts|live)/([^/?]+)", parsed.path)
            if match:
                video_id = match.group(1)

    if re.fullmatch(r"[A-Za-z0-9_-]{6,20}", video_id or ""):
        return f"https://www.youtube-nocookie.com/embed/{video_id}"

    return ""


def inicio(request):
    publicaciones = Publicacion.objects.filter(publicado=True)[:3]
    videos = list(Video.objects.filter(publicado=True)[:6])

    for video in videos:
        video.embed_url = _youtube_embed(video.url)

    return render(request, "index.html", {
        "publicaciones": publicaciones,
        "videos": videos,
    })


def detalle_publicacion(request, slug):
    publicacion = get_object_or_404(
        Publicacion,
        slug=slug,
        publicado=True,
    )
    recientes = (
        Publicacion.objects.filter(publicado=True)
        .exclude(pk=publicacion.pk)[:3]
    )

    return render(request, "publicacion.html", {
        "publicacion": publicacion,
        "publicaciones_recientes": recientes,
    })


def acerca(request):
    return render(request, "acerca.html")


def blog(request):
    publicaciones = Publicacion.objects.filter(publicado=True)
    return render(request, "blog.html", {
        "publicaciones": publicaciones,
    })


def recursos(request):
    return render(request, "recursos.html")


def literatura(request):
    return render(request, "literatura.html")


def naranon(request):
    return render(request, "naranon.html")


def contactos(request):
    return render(request, "contactos.html")
