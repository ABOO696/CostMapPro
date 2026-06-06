import streamlit as st

from app.sidebar import (
    render_sidebar
)
render_sidebar()
st.set_page_config(
    page_title="CostMap Pro",
    layout="wide"
)
st.title("📈 CostMap Pro")

st.write(
    "歡迎使用 CostMap Pro"
    
)



