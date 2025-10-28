from django.http import HttpResponse # type: ignore
from django.shortcuts import render # type: ignore

# Create your views here.
def homePage(request):
    return render(request, "CodeForEachWebpage/HomeScreen.html")

#def engineering(request):
    #return render(request, "CodeForEachWebpage/EngineeringHomePage.html")

#def IED(request):
    #return render(request, "CodeForEachWebpage/IEDCalculator.html")

def POE(request):
    return render(request, "CodeForEachWebpage/POECalculator.html")

#def science(request):
    #return render(request, "CodeForEachWebpage/ScienceHomePage.html")

#def chemistry(request):
    #return render(request, "CodeForEachWebpage/ChemistryHomePage.html")

#def chemistryI(request):
    #return render(request, "CodeForEachWebpage/ChemistryICalculator.html")

#def chemistryIHonors(request):
    #return render(request, "CodeForEachWebpage/ChemistryIHonorsCalculator.html")

def chemistryIACP(request):
    return render(request, "CodeForEachWebpage/ChemistryICalculator.html")

#def math(request):
    #return render(request, "CodeForEachWebpage/MathHomePage.html")

#def algera(request):
    #return render(request, "CodeForEachWebpage/AlgebraHomePage.html")

#def algebraII(request):
    #return render(request, "CodeForEachWebpage/AlgebraIICalculator.html")

def algebraIIHonors(request):
    return render(request, "CodeForEachWebpage/AlgebraIICalculator.html")

def general(request):
    return render(request, "CodeForEachWebpage/GeneralCalculator.html")