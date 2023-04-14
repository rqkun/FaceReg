from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av
import streamlit as st

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{
      "username": "dc2d2894d5a9023620c467b0e71cfa6a35457e6679785ed6ae9856fe5bdfa269",
      "credential": "tE2DajzSJwnsSbc123",
      "urls": "turn:global.turn.twilio.com:3478?transport=udp"
    }]}
)

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")
 
webrtc_ctx = webrtc_streamer(
    key="WYH", #WYH
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,
)
