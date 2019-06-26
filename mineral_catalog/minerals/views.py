import random

from django.shortcuts import render, get_object_or_404

from .models import Mineral

# Create your views here.
def minerals_home(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/minerals_home.html',
                  {'title': 'Home', 'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/minerals_detail.html',
                  {'title': mineral, 'mineral': mineral})


def mineral_random(request):
    minerals = Mineral.objects.all()
    mineral = random.choice(minerals)
    return render(request, 'minerals/minerals_detail.html',
                  {'title': mineral, 'mineral': mineral})
