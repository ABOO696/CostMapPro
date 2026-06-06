# app/sidebar.py

import streamlit as st

def render_sidebar():

    with st.sidebar:

        st.title("📈 CostMap Pro")

        st.caption("V1.5")

        st.divider()

        st.write("導航")


        st.page_link(
            "app/pages/Dashboard.py",
            label="📊 Dashboard"
        )

        st.page_link(
            "app/pages/Radar.py",
            label="🎯 Radar"
        )

        st.page_link(
            "app/pages/CostMap.py",
            label="🗺 CostMap"
        )

        st.page_link(
            "app/pages/Analysis.py",
            label="🔍 Analysis"
        )
