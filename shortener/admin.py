from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib import admin
from django.db import IntegrityError, transaction
from .utils import generate_code

from .models import Short


@admin.register(Short)
class ShortAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "url",
    )

    def save_model(self, request, obj, form, change):
        existing = Short.objects.filter(url=obj.url).first()
        if existing:
            self.message_user(request, f"Short for this URL already exists: {existing.code}")
            return

        if not obj.code:
            for _ in range(settings.MAX_ATTEMPTS):
                obj.code = generate_code(obj.url)
                try:
                    with transaction.atomic():
                        super().save_model(request, obj, form, change)
                    return
                except IntegrityError:
                    obj.code = None

            raise ValueError(_("Couldn't generate a unique code."))
        super().save_model(request, obj, form, change)
