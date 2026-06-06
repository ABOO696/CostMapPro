# app/services/api_client.py

import requests

API_URL = "http://localhost:8000"


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