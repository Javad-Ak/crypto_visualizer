from django.shortcuts import render

from core.utils import requests, figures


def index(request):
    return render(request, 'core/index.html')


def overview(request):
    data = requests.get_overview()
    cap = dict(data['market_cap_percentage'])
    del data['total_market_cap']
    del data['updated_at']
    del data['market_cap_percentage']
    del data['total_volume']

    others = 100.0
    for t in cap.values():
        others -= float(t)
    cap['others'] = others
    fig = figures.create_pie(names=cap.keys(), values=cap.values(), title="Market Cap")

    return render(request, 'core/overview.html', context={'data': data, 'fig': fig.to_html(full_html=False)})


def prices(request):
    return render(request, 'core/prices.html')


def search(request, query):
    return render(request, 'core/search.html')
