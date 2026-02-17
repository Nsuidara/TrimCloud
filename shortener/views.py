from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404, redirect

from .models import Short
from .serializers import ShortCreateSerializer


class ShortCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [AllowAny]
    queryset = Short.objects.all()
    serializer_class = ShortCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class ShortRedirectView(generics.GenericAPIView):
    queryset = Short.objects.all()

    def get(self, request, *args, **kwargs):
        short = get_object_or_404(Short, code=kwargs["code"])
        return redirect(short.url)
