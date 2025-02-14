import streamlit as st
import time
import datetime
from PIL import Image
import base64

# Set page config
st.set_page_config(page_title="Valhalla Countdown", layout="wide")

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Load background image
bg_image_base64 = get_base64("valhalla-viking.webp")
bg_style = f"""
    <style>
   .stApp {{
        background: url(data:image/webp;base64,{bg_image_base64}) no-repeat center center fixed;
        background-size: cover;
    }}
    .countdown {{
        font-size: 12rem;
        font-weight: bold;
        font-family: 'Cinzel', serif; /* Norse-styled font */
        color: #FFFFFF;
        text-shadow: 2px 2px 10px #FFD700, 4px 4px 20px black; /* Gold outer glow with dark shadow */
        text-align: center;
    }}
    </style>
"""

st.markdown(bg_style, unsafe_allow_html=True)

# Countdown target date
end_date = datetime.datetime(2025, 2, 19, 23, 59, 59)

# Countdown logic with dynamic update
def countdown_timer():
    countdown_placeholder = st.empty()  # Placeholder to update countdown dynamically
    while True:
        now = datetime.datetime.now()
        time_left = end_date - now
        if time_left.total_seconds() > 0:
        #if False:            
            days, seconds = divmod(time_left.total_seconds(), 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)
            countdown_placeholder.markdown(
                f'<span class="countdown">{int(days)}d {int(hours)}h {int(minutes)}m {int(seconds)}s</span>',
                unsafe_allow_html=True
            )
            time.sleep(1)
        else:
            countdown_placeholder.empty()  # Clear the countdown
            st.balloons()
            st.snow()
            st.markdown('<span class="countdown">Goodbye Valhalla!</span>', unsafe_allow_html=True)
            break

# Run countdown
countdown_timer()
