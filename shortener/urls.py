from django.urls import path
from . import views

app_name = "shortener" 

urlpatterns = [
    path("short", views.ShortCreateView.as_view(), name="short-create"),
    path("shrt/<str:code>", views.ShortRedirectView.as_view(), name="short-redirect"),
]