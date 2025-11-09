from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .utils import pick_random_photo

@login_required
def home(request):
    bg = pick_random_photo()  # imagen de fondo
    return render(request, "home.html", {"bg": bg})

@login_required
def random_photo_api(request):
    p = pick_random_photo()
    if not p:
        return JsonResponse({"ok": False})
    return JsonResponse({"ok": True, "url": p.image.url, "title": p.title or ""})
