import requests


def get_coins(per_page=8, page=1, order='market_cap', desc=True):
    if (per_page > 100 or per_page < 1 or order not in
            ['name', 'market_cap', 'price_change_percentage_24h', 'volume']):
        raise ValueError('Invalid parameters')

    order = order + '_desc' if desc else order + "_asc"
    response = requests.get(url='https://api.coingecko.com/api/v3/coins/markets',
                            headers={'Accept': 'application/json'},
                            params={'vs_currency': 'usd', 'order': order, 'per_page': per_page, 'page': page})
    response.raise_for_status()
    return response.json()


def get_overview():
    response = requests.get(url='https://api.coingecko.com/api/v3/global', headers={'Accept': 'application/json'})
    response.raise_for_status()
    return response.json()['data']


def search_coins(query):
    response = requests.get(url='https://api.coingecko.com/api/v3/search', headers={'Accept': 'application/json'},
                            params={'query': query})
    response.raise_for_status()
    return response.json()['coins'][:10]
