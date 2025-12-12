import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

BASE_DIR = pathlib.Path(__file__).parent
SIMULATORS = {
    "별의 일주운동 시뮬레이터": BASE_DIR / "Stellar Diurnal Simulator.html",
}

selected = "별의 일주운동 시뮬레이터"
html_path = SIMULATORS[selected]

html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=900, scrolling=True)
