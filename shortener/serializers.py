from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from django.core.validators import URLValidator
from django.conf import settings
from django.db import IntegrityError
from typing import Any
from .models import Short
from .utils import generate_code
from .types import ShortData


class ShortCreateSerializer(serializers.ModelSerializer):
    url = serializers.URLField(
        validators=[URLValidator(schemes=["http", "https"])],
        required=True,
        error_messages={
            "required": _("Invalid URL."),
            "blank": _("Invalid URL."),
            "invalid": _("Invalid URL."),
        },
    )

    def create(self, validated_data: ShortData) -> Short:
        url = validated_data["url"]

        short = Short.objects.filter(url=url).first()
        if short:
            return short

        for _ in range(settings.MAX_ATTEMPTS):
            code = generate_code(url)
            try:
                return Short.objects.create(url=url, code=code)
            except IntegrityError:
                continue

        raise serializers.ValidationError(_("Couldn't generate a unique code."))

    class Meta:
        model = Short
        fields = ["url", "code"]
        read_only_fields = ["code"]
