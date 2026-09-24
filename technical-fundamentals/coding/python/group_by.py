"""
We have a set of 100 clients that have purchased various amount of products in our service.
Our analytics platform is not suited for it so we want to build a short script that can always answer a few questions for us:
1. What is the distribution of clients based on the # of orders? (How many purchased 1, 2, 3, etc)
2. What is the mean volume (in $) of our clients total value?

The raw data is a json file at DATA_URL. Each client looks like this:

    {
        "id": "44b92d9b-...",
        "name": "Toby Abernathy",
        "email": "Kimberly92@hotmail.com",
        "orders": [{"id": "ff791a74-...", "price": 614}, ...]
    }

To load it: json.load(urllib.request.urlopen(DATA_URL))
"""

DATA_URL = "https://gist.githubusercontent.com/conanbatt/9da0470db6cf90c61324f8365d448a92/raw/caa9c9e8d365abd374b5d2e1ef0f380b75d45962/.json"


class ClientAnalytics:
    def __init__(self, clients: list[dict]):
        pass

    def orders_distribution(self) -> dict[int, int]:
        """Maps number of orders to number of clients with that many orders."""
        pass

    def mean_client_value(self) -> float:
        """Mean of the sum of order prices of each client."""
        pass


# Tests

CLIENTS = [
    {"id": "1", "name": "Ana", "email": "ana@example.com", "orders": [{"id": "a", "price": 100}]},
    {
        "id": "2",
        "name": "Beto",
        "email": "beto@example.com",
        "orders": [{"id": "b", "price": 50}, {"id": "c", "price": 150}],
    },
    {
        "id": "3",
        "name": "Caro",
        "email": "caro@example.com",
        "orders": [{"id": "d", "price": 10}, {"id": "e", "price": 20}],
    },
    {"id": "4", "name": "Dani", "email": "dani@example.com", "orders": []},
]


def test_orders_distribution():
    assert ClientAnalytics(CLIENTS).orders_distribution() == {0: 1, 1: 1, 2: 2}


def test_mean_client_value():
    # Totals: 100, 200, 30, 0
    assert ClientAnalytics(CLIENTS).mean_client_value() == 82.5
