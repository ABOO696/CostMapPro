from app.services.cost_engine import (
    CostEngine
)


def update_institution_position(
    previous_position,
    previous_cost,
    net_buy,
    close_price
):

    new_position = max(
        previous_position + net_buy,
        0
    )

    if new_position == 0:

        return (
            0,
            0
        )

    new_cost = CostEngine.weighted_cost(
        previous_position,
        previous_cost,
        max(net_buy, 0),
        close_price
    )

    return (
        new_position,
        new_cost
    )