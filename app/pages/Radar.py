import streamlit as st
import pandas as pd
from app.sidebar import (
    render_sidebar
)

render_sidebar()
from app.services.stock_service import (
    StockService
)

st.title("🎯 Radar")

rows = StockService.radar()

data = []

for row in rows:

    data.append({

        "Stock":
        row.stock_id,

        "Score":
        float(row.cost_score),

        "Major":
        float(row.major_cost),

        "Retail":
        float(row.retail_cost),

        "Gap":
        float(row.cost_gap)
    })

df = pd.DataFrame(data)

st.dataframe(
    df,
    use_container_width=True
)
