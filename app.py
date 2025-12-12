import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

BASE_DIR = pathlib.Path(__file__).parent
SIMULATORS = {
    "별의 일주운동 (Stellar Diurnal Simulator.html)": BASE_DIR / "Stellar Diurnal Simulator.html",
    "지구 열수지 평형 (Earth Heat Balance Simulator.html)": BASE_DIR / "Earth Heat Balance Simulator.html",
}

selection = st.sidebar.selectbox("시뮬레이터 선택", list(SIMULATORS.keys()))
html_content = SIMULATORS[selection].read_text(encoding="utf-8")
components.html(html_content, height=900, scrolling=True)
