# import streamlit as st
# import paho.mqtt.client as mqtt
# import time

# # MQTT broker details
# mqtt_broker = "YOUR_MQTT_BROKER_IP"
# mqtt_topic = "sensor_data"

# # MQTT client setup
# mqtt_client = mqtt.Client()

# # Variable to store the latest data from NodeMCU
# latest_data = None

# def on_connect(client, userdata, flags, rc):
#     st.write("Connected to MQTT broker")
#     mqtt_client.subscribe(mqtt_topic)

# def on_message(client, userdata, message):
#     global latest_data
#     latest_data = int(message.payload.decode())

# # Streamlit app
# def main():
#     st.title("NodeMCU Real-Time Dashboard")

#     # Connect to MQTT broker
#     mqtt_client.on_connect = on_connect
#     mqtt_client.on_message = on_message
#     mqtt_client.connect(mqtt_broker, 1883)
#     mqtt_client.loop_start()

#     st.write("Waiting for data...")

#     # Real-time dashboard
#     chart = st.line_chart([], use_container_width=True)

#     # Update dashboard with new data
#     while True:
#         if latest_data is not None:
#             chart.add_rows([[time.time(), latest_data]])
#             latest_data = None
#         st.sleep(1)

# if __name__ == "__main__":
#     main()