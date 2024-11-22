import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

try:
    if place:
    # Get temperature/sky data
        filtered_content = get_data(place, days)

        # Create a tempearture plot
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] /10 for dict in filtered_content]
            dates = [dict["dt_txt"] for dict in filtered_content]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date",\
                                            "y":"Temperature (C)"})
            st.plotly_chart(figure)
        elif option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_content]
            images = {"Clear":"images/clear.png", "Clouds":"images/cloud.png",
                    "Rain":"images/rain.png", "Snow":"images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
except KeyError:
    st.warning("That city does not exist, try again!", icon="⚠️")