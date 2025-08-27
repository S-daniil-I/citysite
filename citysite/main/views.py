from django.shortcuts import render

from main.models import Enterprise, Leisure


def index(request):
    return render(request, 'main/index.html')

def enterprises(request):
    enterprises_list = Enterprise.objects.all()
    return render(request, 'main/enterprises.html', {'enterprises': enterprises_list})

def sport(request):
    return render(request, 'main/sport.html')

def leisure(request):
    leisure_list= Leisure.objects.all()
    return render(request, 'main/leisure.html', {'leisures': leisure_list})


def services(request):
    return render(request, 'main/services.html')
