import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Webcam Stream")

webrtc_streamer(key="webcam")
