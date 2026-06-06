# app.py

import streamlit as st

from app.sidebar import (
    render_sidebar
)

render_sidebar()


st.set_page_config(
    page_title="CostMap Pro",
    layout="wide"
)

st.title("📈 CostMap Pro V1.5")

st.markdown("""
### 主力成本雷達系統

使用左側選單進入：

- Dashboard
- Radar
- CostMap
- Analysis
""")
