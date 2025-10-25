from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("engineering/", views.engineering, name="engineeringCalculator"),
    path("science/", views.science, name="scienceCalculator"),
    path("math/", views.math, name="mathCalculator"),
    path("general/", views.general, name="generalCalculator"),
]