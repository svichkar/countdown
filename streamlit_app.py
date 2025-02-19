import streamlit as st
import time
import datetime
from PIL import Image
import base64
import pytz

# Set page config
st.set_page_config(page_title="Valhalla", layout="wide", page_icon="favicon.ico")

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

    .digital-card {{
            font-family: 'Courier New', monospace;
            font-size: 10vw; /* Scale font size based on viewport width */
            background-color: rgba(0, 0, 0, 0.5);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transform: translateY(0);
            transition: transform 0.5s ease-in-out;
        }}
        .digital-card:hover {{
            transform: translateY(-20px);
    }}

    .timer-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        flex-wrap: wrap; /* Allow wrapping on smaller screens */
    }}

    /* Adjust layout for smaller screens */
    @media (max-width: 768px) {{
        .digital-card {{
            font-size: 15vw; /* Larger font size for mobile */
            padding: 10px;
        }}
    }}

    @media (max-width: 480px) {{
        .digital-card {{
            font-size: 20vw; /* Even larger font size for very small screens */
            padding: 5px;
        }}
    }}
    </style>
"""

st.markdown(bg_style, unsafe_allow_html=True)

# Set Kyiv timezone
kyiv_tz = pytz.timezone("Europe/Kyiv")

# Countdown target date
end_date = kyiv_tz.localize(datetime.datetime(2025, 2, 19, 18, 59, 59))

# Countdown logic with dynamic update
def countdown_timer():
    countdown_placeholder = st.empty()  # Placeholder to update countdown dynamically
    while True:
        now = datetime.datetime.now(kyiv_tz)
        time_left = end_date - now
        if time_left.total_seconds() > 0:
            days, seconds = divmod(time_left.total_seconds(), 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)

            # Display the rolling digital cards
            countdown_placeholder.markdown(
                f"""
                <div class="timer-container">
                    <div class="digital-card">{int(days):02}d</div>
                    <div class="digital-card">{int(hours):02}h</div>
                    <div class="digital-card">{int(minutes):02}m</div>
                    <div class="digital-card">{int(seconds):02}s</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            time.sleep(1)
        else:
            countdown_placeholder.empty()  # Clear the countdown
            st.balloons()
            st.snow()
            countdown_placeholder.markdown('<span class="countdown">Goodbye Valhalla!</span>', unsafe_allow_html=True)
            break

# Run countdown
countdown_timer()
