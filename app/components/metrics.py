import streamlit as st

def show_metrics(
    total_stock,
    radar_stock,
    avg_score,
    bullish_count
):

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "股票數",
        total_stock
    )

    c2.metric(
        "雷達股",
        radar_stock
    )

    c3.metric(
        "平均分數",
        avg_score
    )

    c4.metric(
        "多頭數",
        bullish_count
    )