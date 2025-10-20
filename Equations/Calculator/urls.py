from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("engineering/", views.engineering, name="engineeringCalculator")
]