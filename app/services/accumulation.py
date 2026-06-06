def accumulation_score(

    foreign_buy,

    trust_buy,

    dealer_buy,

    margin_change,

    momentum

):

    score = 50

    if foreign_buy > 0:

        score += 15

    if trust_buy > 0:

        score += 10

    if dealer_buy > 0:

        score += 5

    if margin_change < 0:

        score += 10

    if momentum > 0:

        score += 10

    return min(
        score,
        100
    )