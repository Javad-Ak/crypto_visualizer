from django.shortcuts import render

from core.utils import requests, figures


def index(request):
    return render(request, 'core/index.html')


def overview(request):
    data, fig = figures.market_overview()
    return render(request, 'core/overview.html',
                  context={'data': data, 'fig': fig.to_html(full_html=False, config={'displayModeBar': False})})


def prices(request):
    page = request.GET.get('page', 1)
    data = figures.price_overview(page=page)
    context = {'data': data[0], 'figs': data[:1]}
    return render(request, 'core/prices.html', context=context)


def search(request, query):
    data = requests.search_coins(query)
    return render(request, 'core/search.html', context={'data': data})
