import streamlit as st
import streamlit as st
from PIL import Image
import helper as help
import time
import numpy as np
import pandas as pd
import plost
import plotly.express as px
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import requests
import paho.mqtt.client as mqtt

def dashboard():
   st.header("Real-Time / Live Data Dashboard")
    # Fetch data from ThingSpeak
channel_id = 2173442
api_key = 'AV6YQ3I1UJCYLUQ5'

    # Define the ThingSpeak API URL
api_url = f'https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={api_key}'

    # Make a GET request to fetch the data from ThingSpeak
response = requests.get(api_url)
data = response.json()

    # Extract the field values from the response
field1 = [entry['field1'] for entry in data['feeds']]
field2 = [entry['field2'] for entry in data['feeds']]
field3 = [entry['field3'] for entry in data['feeds']]   
field4 = [entry['field4'] for entry in data['feeds']]



timestamps = [entry['created_at'] for entry in data['feeds']]

    # Create a DataFrame from the extracted data
df = pd.DataFrame({'Field1': field1, 'Field2': field2,'Field3': field3, 'Field4': field4, 'Timestamp': timestamps})

    # Display the data in Streamlit
st.title('ThingSpeak Data')
st.dataframe(df)
