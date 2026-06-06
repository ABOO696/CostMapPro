import pandas as pd


def calculate_momentum(
    cost_series
):

    if len(cost_series) < 20:

        return 0

    s = pd.Series(cost_series)

    ma5 = s.tail(5).mean()

    ma20 = s.tail(20).mean()

    return round(
        ma5 - ma20,
        2
    )