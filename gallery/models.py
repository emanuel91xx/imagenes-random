from django.db import models

# Create your models here.

class Photo(models.Model):
    image = models.ImageField(upload_to="photos/")
    title = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title or self.image.name