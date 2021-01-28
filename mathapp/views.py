from django.shortcuts import render

# Create your views here.

def cylindervolume(request):
    context = {}
    return render(request, 'mathapp/cylindervolume.html', context)

def areaoftriangle(request):
    context = {}
    return render(request, 'mathapp/areaoftriangle.html', context)

    