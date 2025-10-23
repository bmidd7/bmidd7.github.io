from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

# Create your views here.
def home(request):
    return HttpResponse("Welcome to my site!")

def index(request):
    return render(request, "CodeForEachWebpage/HomeScreen.html")

def engineering(request):
    return render(request, "CodeForEachWebpage/EngineeringCalculator.html")