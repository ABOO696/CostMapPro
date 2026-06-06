import streamlit as st

from app.sidebar import (
    render_sidebar
)

render_sidebar()

from app.components.gauges import (
    cost_score_gauge
)

st.title("Analysis")

stock_id = st.text_input(
    "Stock ID",
    value="2330"
)

row = get_stock_analysis(
    stock_id
)

if row:

    score = row["cost_score"]

    st.plotly_chart(
        cost_score_gauge(score),
        use_container_width=True
    )

    st.metric(
        "Cost Score",
        score
    )

else:

    st.warning(
        "查無資料"
    )
