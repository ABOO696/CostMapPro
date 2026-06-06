from decimal import Decimal


class CostEngine:

    @staticmethod
    def weighted_cost(
        current_position: int,
        current_cost: float,
        net_buy: int,
        price: float
    ) -> float:

        if current_position <= 0:

            return round(price, 2)

        if net_buy <= 0:

            return round(current_cost, 2)

        total_cost = (
            Decimal(current_position)
            *
            Decimal(current_cost)
        ) + (
            Decimal(net_buy)
            *
            Decimal(price)
        )

        total_position = (
            current_position
            +
            net_buy
        )

        return round(
            float(
                total_cost /
                Decimal(total_position)
            ),
            2
        )