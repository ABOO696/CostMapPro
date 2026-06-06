import streamlit as st

from app.sidebar import (
    render_sidebar
)

st.set_page_config(
    page_title="CostMap Pro",
    layout="wide"
)

render_sidebar()
