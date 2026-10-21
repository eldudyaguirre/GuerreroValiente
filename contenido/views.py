from django.shortcuts import render


def inicio(request):
    return render(request, "index.html")


def acerca(request):
    return render(request, "acerca.html")


def blog(request):
    return render(request, "blog.html")


def recursos(request):
    return render(request, "recursos.html")


def naranon(request):
    return render(request, "naranon.html")


def contactos(request):
    return render(request, "contactos.html")
