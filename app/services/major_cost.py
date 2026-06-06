def calculate_major_cost(

    foreign_position,
    foreign_cost,

    trust_position,
    trust_cost,

    dealer_position,
    dealer_cost

):

    total_position = (

        foreign_position

        +

        trust_position

        +

        dealer_position
    )

    if total_position == 0:

        return 0

    total_cost = (

        foreign_position
        *
        foreign_cost

        +

        trust_position
        *
        trust_cost

        +

        dealer_position
        *
        dealer_cost
    )

    return round(
        total_cost
        /
        total_position,
        2
    )