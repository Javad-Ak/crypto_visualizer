import requests


def get_coins(per_page=8, page=1, order='market_cap', desc=True):
    if (per_page > 100 or per_page < 1 or order not in
            ['name', 'market_cap', 'volume', 'price_change_percentage_24h']):
        raise ValueError('Invalid parameters')

    if order == 'price_change_percentage_24h':
        response = requests.get(url='https://api.coingecko.com/api/v3/coins/markets',
                                headers={'Accept': 'application/json'},
                                params={'vs_currency': 'usd', 'order': 'market_cap', 'per_page': 200, 'page': 1})
        response.raise_for_status()
        data = response.json()
        return sorted(data, key=lambda x: x['price_change_percentage_24h'], reverse=desc)[:6]
    else:
        order = order + '_desc' if desc else order + "_asc"
        response = requests.get(url='https://api.coingecko.com/api/v3/coins/markets',
                                headers={'Accept': 'application/json'},
                                params={'vs_currency': 'usd', 'order': order, 'per_page': per_page, 'page': page})
        response.raise_for_status()
        return response.json()


def get_largest_changes(count=6, desc=True):
    data = get_coins(per_page=240)
    return sorted(data, key=lambda x: x['price_change_percentage_24h'], reverse=desc)[:count]


def get_overview():
    response = requests.get(url='https://api.coingecko.com/api/v3/global', headers={'Accept': 'application/json'})
    response.raise_for_status()
    return response.json()['data']


def search_coins(query):
    response = requests.get(url='https://api.coingecko.com/api/v3/search', headers={'Accept': 'application/json'},
                            params={'query': query})
    response.raise_for_status()
    return response.json()['coins'][:10]
