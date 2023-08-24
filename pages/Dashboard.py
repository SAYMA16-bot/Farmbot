import streamlit as stm
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
stm.title("Real-Time / Live Data Dashboard")
Moisture = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

# Row A
a1, a2,a3,a4 = st.columns(4)
a1.metric("Standard Temperature", "28°C", "24°C")
a2.metric("Standard Humidity", "86%", "4%")
a3.metric("Standard Moisture", "80%", "60%")
a4.metric("Standard pH", "86%", "4%")




# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Humidity", "9 mph", "-8%")
b3.metric("pH", "86%", "4%")
b4.metric("Moisture", "86%", "4%")

# Row C
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=Moisture,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(
        data=stocks,
        theta='q2',
        color='company')

