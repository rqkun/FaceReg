from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av
import streamlit as st

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")
 
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")

webrtc_ctx = webrtc_streamer(
    key="example", #WYH
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    #video_processor_factory=VideoProcessor,
    video_frame_callback=video_frame_callback,
    async_processing=True,
)
