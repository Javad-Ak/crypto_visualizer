from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def overview(request):
    return render(request, 'core/overview.html')


def prices(request):
    return render(request, 'core/prices.html')


def search(request, query):
    return render(request, 'core/search.html')
