import streamlit as st

from app.components.metrics import (
    show_metrics
)

st.title("Dashboard")

show_metrics(
    total_stock=1800,
    radar_stock=50,
    avg_score=67.3,
    bullish_count=328
)