import streamlit as st
import pandas as pd

from app.components.charts import (
    cost_chart,
    cost_gap_chart
)

st.title("CostMap")

stock_id = st.text_input(
    "Stock",
    "2330"
)

# TODO DB Query

df = pd.DataFrame()

if not df.empty:

    st.plotly_chart(
        cost_chart(df),
        use_container_width=True
    )

    st.plotly_chart(
        cost_gap_chart(df),
        use_container_width=True
    )