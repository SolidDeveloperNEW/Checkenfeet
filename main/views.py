from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView


class HomePage(ListView):
    model = Banner
    template_name = 'index.html'


def index(request):
    banners = Banner.objects.all().order_by('-id')[:3]
    context = {
        'banners': banners,
    }
    return render(request, 'index.html', context)

