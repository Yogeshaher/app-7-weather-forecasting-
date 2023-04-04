import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast For The Next Days")
place = st.text_input("place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

d, t = get_data(place, days, option)

figure = px.line(x=d, y=t, labels={"x": "date", "y": "temperature (c)"})
st.plotly_chart(figure)
