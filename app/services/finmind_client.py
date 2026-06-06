import os
import requests

class FinMindClient:

    BASE_URL = "https://api.finmindtrade.com/api/v4/data"

    def __init__(self):

        self.token = os.getenv("FINMIND_TOKEN")

        if not self.token:
            raise ValueError(
                "FINMIND_TOKEN not found"
            )

    def get(
        self,
        dataset,
        data_id=None,
        start_date=None,
        end_date=None
    ):

        params = {
            "dataset": dataset,
            "token": self.token
        }

        if data_id:
            params["data_id"] = data_id

        if start_date:
            params["start_date"] = start_date

        if end_date:
            params["end_date"] = end_date

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=60
        )

        response.raise_for_status()

        result = response.json()

        return result["data"]