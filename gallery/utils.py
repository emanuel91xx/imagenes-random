import random
from .models import Photo

def pick_random_photo():
    ids = list(Photo.objects.values_list("id", flat=True))
    if not ids:
        return None
    p = Photo.objects.get(id=random.choice(ids))
    return p
