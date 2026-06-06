# app/sidebar.py

import streamlit as st

def render_sidebar():

    with st.sidebar:
        st.title("📈 CostMap Pro")
        st.caption("V1.5")
        st.divider()
        st.write("導航")

        dashboard = st.Page(
            "app/pages/Dashboard.py",
            title="Dashboard"
        )
        radar = st.Page(
            "app/pages/Radar.py",
            title="Radar"
        )
        costmap = st.Page(
            "app/pages/CostMap.py",
            title="CostMap"
        )
        analysis = st.Page(
            "app/pages/Analysis.py",
            title="Analysis"
        )

pg = st.navigation(
    [dashboard, radar,costmap,analysis]
)

pg.run()
