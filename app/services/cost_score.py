def calculate_cost_score(

    close_price,

    major_cost,

    retail_cost,

    accumulation,

    momentum

):

    score = 50

    if close_price > major_cost:

        score += 10

    if close_price > retail_cost:

        score += 10

    score += (
        accumulation * 0.2
    )

    score += (
        momentum * 0.5
    )

    return round(
        min(score, 100),
        2
    )