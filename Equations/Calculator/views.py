from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

# Create your views here.
def index(request):
    return render(request, "CodeForEachWebpage/HomeScreen.html")

def engineering(request):
    return render(request, "CodeForEachWebpage/EngineeringCalculator.html")

def science(request):
    return render(request, "CodeForEachWebpage/ScienceCalculator.html")

def math(request):
    return render(request, "CodeForEachWebpage/MathCalculator.html")

def general(request):
    return render(request, "CodeForEachWebpage/GeneralCalculator.html")