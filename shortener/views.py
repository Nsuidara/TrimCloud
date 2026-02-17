from typing import Any
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Short
from .serializers import ShortCreateSerializer
from .types import CodeKwargs


class ShortCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [AllowAny]
    queryset = Short.objects.all()
    serializer_class = ShortCreateSerializer

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.create(request, *args, **kwargs)


class ShortRedirectView(generics.GenericAPIView):
    queryset = Short.objects.all()

    def get(
        self, request: HttpRequest, *args: Any, **kwargs: CodeKwargs
    ) -> HttpResponseRedirect:
        short = get_object_or_404(Short, code=kwargs["code"])
        return redirect(short.url)
