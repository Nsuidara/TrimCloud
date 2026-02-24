from typing import Any
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Short
from .serializers import ShortCreateSerializer
from .types import CodeKwargs


class ShortCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Short.objects.all()
    serializer_class = ShortCreateSerializer


class ShortRedirectView(generics.GenericAPIView):
    queryset = Short.objects.all()

    def get(
        self, request: HttpRequest, *args: Any, **kwargs: CodeKwargs
    ) -> HttpResponseRedirect:
        short = get_object_or_404(Short, code=kwargs["code"])
        return redirect(short.url)
