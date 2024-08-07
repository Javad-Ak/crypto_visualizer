from plotly import express as px

from core.utils import requests


def market_overview():
    data = requests.get_overview()
    cap = dict(data['market_cap_percentage'])
    del data['total_market_cap']
    del data['updated_at']
    del data['market_cap_percentage']
    del data['total_volume']
    data = {str(k).replace("_", " ").title(): v for k, v in data.items()}

    others = 100.0
    for t in cap.values():
        others -= float(t)
    cap['others'] = others

    df = [{'coin': coin, 'market_cap': market_cap} for coin, market_cap in cap.items()]
    print(df)
    fig = px.treemap(df, path=[px.Constant('Market'), 'coin'], values='market_cap', title='Crypto Market Cap',
                     labels={'market_cap': 'Market Cap', 'id': 'Coin'})
    fig.update_layout(
        font_color="grey",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    return data, fig


def price_overview():
    return (requests.get_coins(per_page=100, page=1),
            coin_bar_fig("Total Volume", order='volume', desc=True),
            coin_bar_fig("Highest Growth 24h", order='price_change_percentage_24h', desc=True),
            coin_bar_fig('Largest Drop 24h', order='price_change_percentage_24h', desc=False),)


def coin_bar_fig(title, count=6, order='market_cap', desc=True):
    data = requests.get_coins(per_page=count, page=1, order=order, desc=desc)
    if order == 'volume':
        order = 'total_volume'

    fig = px.bar(data, x='symbol', y=order, title=title)
    fig.update_layout(
        font_color="grey",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    return fig
