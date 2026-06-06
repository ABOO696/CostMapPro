from app.services.cost_engine import (
    CostEngine
)

def update_retail_cost(
    previous_balance,
    previous_cost,
    balance_today,
    margin_change,
    close_price
):

    if balance_today <= 0:

        return 0

    if previous_balance == 0:

        return close_price

    if margin_change > 0:

        return CostEngine.weighted_cost(
            previous_balance,
            previous_cost,
            margin_change,
            close_price
        )

    return previous_cost