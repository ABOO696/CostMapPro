# app/services/api_client.py

import requests

API_URL = "http://localhost:8000"

def get_stock_analysis(stock_id):

    try:

        response = requests.get(
            f"{API_URL}/costmap/{stock_id}"
        )

        response.raise_for_status()

        data = response.json()

        if len(data) == 0:
            return None

        return data[-1]

    except Exception as e:

        print(e)

        return None
        

def get_radar():

    return requests.get(
        f"{API_URL}/radar"
    ).json()


def get_dashboard():

    return requests.get(
        f"{API_URL}/dashboard"
    ).json()


def get_costmap(
    stock_id
):

    return requests.get(
        f"{API_URL}/costmap/{stock_id}"
    ).json()
