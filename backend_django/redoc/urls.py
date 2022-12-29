from django.urls import path
from backend_django.redoc.views import redoc, redoc_json

urlpatterns = [
    path("", redoc),
    path("json/", redoc_json)
]