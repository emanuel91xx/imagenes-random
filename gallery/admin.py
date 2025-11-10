import os

from django import forms
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Photo


class AdminMultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


# Register your models here.


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "created_at")
    search_fields = ("title",)
    exclude = ("title",)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None and "image" in form.base_fields:
            form.base_fields["image"].widget = AdminMultipleFileInput(attrs={"multiple": True})
        return form

    def add_view(self, request, form_url="", extra_context=None):
        if request.method == "POST" and request.FILES.getlist("image"):
            files = request.FILES.getlist("image")
            created = 0
            for f in files:
                title, _ = os.path.splitext(os.path.basename(f.name))
                Photo.objects.create(image=f, title=title)
                created += 1
            if created:
                self.message_user(
                    request, f"Se subieron {created} imágenes.", level=messages.SUCCESS
                )
            changelist_url = reverse("admin:gallery_photo_changelist")
            return HttpResponseRedirect(changelist_url)
        return super().add_view(request, form_url, extra_context)
