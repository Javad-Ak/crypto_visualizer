from plotly import express as px

from core.utils import requests


def market_overview():
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

    df = {'coins': data.keys(), 'market cap': data.values()}
    fig = px.treemap(df, path=['coins'], values='market cap', title='Market Cap')
    return data, fig


def price_overview(per_page=20, page=1):
    return (requests.get_coins(per_page=per_page, page=page),
            coin_bar_fig("Trade Volume 24h", order='volume', desc=True),
            coin_bar_fig("Highest Growth 24h", order='price_change_percentage_24h', desc=True),
            coin_bar_fig('Largest Drop 24h', order='price_change_percentage_24h', desc=False),)


def coin_bar_fig(title, count=6, order='market_cap', desc=True):
    data = requests.get_coins(per_page=count, page=1, order=order, desc=desc)
    if order == 'volume':
        order = 'total_volume'

    return px.bar(data, x='name', y=order, title=title)
