from typing import Dict

from .models import Photo


def random_photos(request) -> Dict[str, str]:
    """
    Provides random image URLs for background and logo from Photo model.
    If there are no photos, returns empty strings so templates can fallback.
    """
    bg_url = ""
    logo_url = ""
    try:
        # Using two potentially different random photos for variety
        bg = Photo.objects.order_by("?").first()
        logo = Photo.objects.order_by("?").first()
        if bg and getattr(bg, "image", None):
            try:
                bg_url = bg.image.url
            except Exception:
                bg_url = ""
        if logo and getattr(logo, "image", None):
            try:
                logo_url = logo.image.url
            except Exception:
                logo_url = ""
    except Exception:
        # Be resilient if DB not ready / migrations pending
        bg_url = ""
        logo_url = ""

    return {
        "random_bg_url": bg_url,
        "random_logo_url": logo_url,
    }
