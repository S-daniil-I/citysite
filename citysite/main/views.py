from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def enterprises(request):
    return render(request, 'main/enterprises.html')

def sport(request):
    return render(request, 'main/sport.html')

def leisure(request):
    return render(request, 'main/leisure.html')

def services(request):
    return render(request, 'main/services.html')
