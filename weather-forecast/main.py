import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

#def get_data(days):
#    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
##    temperature = [10, 15, 25]
#    temperature = [days * i for i in temperature]
#    return dates, temperature

date = get_data(place, days, option)

d, t = get_data(days)
figure = px.line(x=d, y=t,labels={"x": "Date",\
                                  "y":"Temperature (C)"})
st.plotly_chart(figure)