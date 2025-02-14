import streamlit as st
import time
import datetime
from PIL import Image

# Set page config
st.set_page_config(page_title="Valhalla Countdown", layout="wide")

# Load background image
bg_image = "valhalla-viking.webp"  # Image located in the same directory as main script
bg_style = f"""
    <style>
    .stApp {{
        background: url({bg_image}) no-repeat center center fixed;
        background-size: cover;
    }}
    .countdown {{
        font-size: 200px;
        font-weight: bold;
        color: #FFD700;
        text-shadow: 6px 6px 12px black;
        text-align: center;
    }}
    </style>
"""

st.markdown(bg_style, unsafe_allow_html=True)

# Countdown target date
end_date = datetime.datetime(2025, 2, 19, 23, 59, 59)

# Countdown logic
def countdown_timer():
    now = datetime.datetime.now()
    time_left = end_date - now
    if time_left.total_seconds() > 0:
        days, seconds = divmod(time_left.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        st.markdown(f'<span class="countdown">{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s</span>', unsafe_allow_html=True)
    else:
        st.balloons()
        st.snow()
        st.markdown("<h1 style='text-align: center; color: gold;'>Goodbye Valhalla!</h1>", unsafe_allow_html=True)

# Run countdown
countdown_timer()

# Auto-refresh every second
st.rerun() if datetime.datetime.now() < end_date else None
