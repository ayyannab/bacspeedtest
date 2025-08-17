import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <h3 style="color:white; text-align:center;">
        BAC's Speed Test by Ookla
    </h3>
    <iframe src="https://bacn.speedtestcustom.com/" width="100%" height="1000px" style="border:none;"></iframe>
    <h4 style="color:white; text-align:center;">©️ BAC speedtest</h4>
    """,
    unsafe_allow_html=True
)
