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
    "2330"
)

score = 91

st.plotly_chart(
    cost_score_gauge(score),
    use_container_width=True
)

st.metric(
    "Cost Score",
    score
)
