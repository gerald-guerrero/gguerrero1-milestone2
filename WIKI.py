import requests
import itertools

def wiki_data(title):
    BASE_URL = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "format": "json",
        "search": title,
        "namespace": "-2",
        "limit": "1"
    }

    response = requests.get(
        BASE_URL, params=params
    )

    # source: https://www.geeksforgeeks.org/python-itertools-chain/
    response_json = list(itertools.chain.from_iterable(response.json()))

    for item in response_json:
        if "wikipedia.org" in item:
            return item
    return "URL not found"
