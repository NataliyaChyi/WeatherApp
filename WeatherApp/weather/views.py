from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html')

def new_address(request):
    return render(request, 'weather/new_address.html')

