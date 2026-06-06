import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("📈 CostMap Pro")

        st.caption("Version 1.5 MVP")

        st.divider()

        stock_id = st.text_input(
            "股票代號",
            value=st.session_state.get(
                "selected_stock",
                "2330"
            )
        )

        st.session_state[
            "selected_stock"
        ] = stock_id

        st.divider()

        st.markdown("### 系統資訊")

        st.success("API Online")

        st.caption(
            "FinMind Data Source"
        )

        st.caption(
            "Daily Update 20:00"
        )

        st.divider()

        st.markdown("### 快速篩選")

        min_score = st.slider(
            "最低 Cost Score",
            min_value=0,
            max_value=100,
            value=80
        )

        st.session_state[
            "min_score"
        ] = min_score
