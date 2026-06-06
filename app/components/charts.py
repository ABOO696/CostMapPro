import plotly.graph_objects as go


def cost_chart(df):

    fig = go.Figure()

    fig.add_scatter(
        x=df.trade_date,
        y=df.close_price,
        name="Close"
    )

    fig.add_scatter(
        x=df.trade_date,
        y=df.major_cost,
        name="Major"
    )

    fig.add_scatter(
        x=df.trade_date,
        y=df.retail_cost,
        name="Retail"
    )

    return fig

def cost_gap_chart(df):

    fig = go.Figure()

    fig.add_bar(
        x=df.trade_date,
        y=df.cost_gap
    )

    return fig


