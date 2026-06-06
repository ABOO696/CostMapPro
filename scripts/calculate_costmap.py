stocks = get_all_stocks()

for stock in stocks:

    calculate_stock_costmap(
        stock.stock_id
    )


def calculate_stock_costmap(
    stock_id
):

    prices = load_prices(
        stock_id
    )

    institutions = load_institutions(
        stock_id
    )

    margins = load_margins(
        stock_id
    )

    for day in trading_days:

        update_foreign_cost()

        update_trust_cost()

        update_dealer_cost()

        update_retail_cost()

        major_cost = (
            calculate_major_cost(...)
        )

        gap = (
            major_cost
            -
            retail_cost
        )

        accumulation = (
            accumulation_score(...)
        )

        score = (
            calculate_cost_score(...)
        )

        save_cost_map(...)

