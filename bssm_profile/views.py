from django.shortcuts import render
from .models import Project


def home(request):
    context = {
        'projekte': Project.objects.all()
    }
    return render(request, 'bssm_profile/home.html', context)

def about(request):
    return render(request, 'bssm_profile/about.html', {'title': 'Alles über'})