import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor


# Set the title for the Streamlit app
st.title("Video Capture with OpenCV")
model=YOLO("C:/Users/LENOVO/Downloads/weed.pt")

# Use this line to capture video from the webcam (adjust the index if needed)
cap = cv2.VideoCapture(1)

frame_placeholder = st.empty()

# Add a "Stop" button and store its state in a variable
stop_button_pressed = st.button("Stop")

while cap.isOpened() and not stop_button_pressed:
    ret, frame = cap.read()

    if not ret:
        st.write("The video capture has ended.")
        break

    # You can process the frame here if needed
    # e.g., apply filters, transformations, or object detection
    # For object detection, you should use your Ultralytics YOLO model separately.

    # Convert the frame from BGR to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame using Streamlit's st.image
    frame_placeholder.image(frame, channels="RGB")

    # Break the loop if the 'q' key is pressed or the user clicks the "Stop" button
    if cv2.waitKey(1) & 0xFF == ord("q") or stop_button_pressed: 
        break

cap.release()
cv2.destroyAllWindows()

# Perform object detection using Ultralytics YOLO model
# You can use your YOLO model separately here.
