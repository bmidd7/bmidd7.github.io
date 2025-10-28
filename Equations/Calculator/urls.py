from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.homePage, name="HomePage"),
    #path("Engineering/", views.engineering, name="engineeringHomePage"),
    #path("Engineering/Intro-to-Engineering-Design", views.IED, name="introToEngineeringDesignCalculator"),
    path("Engineering/Principles-of-Engineering/", views.POE, name="principlesOfEngineeringCalculator"),
    #path("Science/", views.science, name="scienceHomePage"),
    #path("Science/Chemistry/", views.chemistry, name="chemistryHomePage"),
    #path("Science/Chemistry/Chemisty-I", views.chemistryI, name="chemistryICalculator"),
    #path("Science/Chemistry/Chemisty-I-Honors", views.chemistryIHonors, name="chemistryIHonorsCalculator"),
    path("Science/Chemistry/ACP-Chemistry-I-Honors/", views.chemistryIACP, name="chemistryIACPCalculator"),
    #path("Math/", views.math, name="mathHomePage"),
    #path("Math/Algebra", views.algera, name="algebraHomePage"),
    #path("Math/Algebra/Algebra-II/", views.algebraII, name="algebraIICalculator"),
    path("Math/Algebra/Algebra-II-Honors/", views.algebraIIHonors, name="algebraIIHonorsCalculator"),
    path("General/", views.general, name="generalCalculator"),
]