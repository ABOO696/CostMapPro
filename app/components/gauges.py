import plotly.graph_objects as go

def cost_score_gauge(
    score
):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            title={
                "text":"Cost Score"
            }
        )
    )

    return fig