import streamlit as st
import plotly.express as px
from backend import get_data

st.header("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        with st.spinner("Fetching weather data..."):
            filtered_data = get_data(place, days)

            if option == "Temperature":
                # Convert temperatures from Kelvin to Celsius
                temperatures = [dict['main']['temp'] - 273.15 for dict in filtered_data]
                dates = [dict['dt_txt'] for dict in filtered_data]
                figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature in °C"})  # Creates a line graph
                st.plotly_chart(figure)
            else:
                sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
                images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
                image_paths = [images[condition] for condition in sky_conditions]
                st.image(image_paths, width=115)
    except KeyError:
        st.write("Uh Oh! Such place doesn't exist in OpenWeather database")
    except ConnectionError as ce:
        st.error(str(ce))
    except ValueError as ve:
        st.error(str(ve))
    except RuntimeError as re:
        st.error(str(re))
    except Exception as e:
        st.error("Connection failed. The OpenWeather server might be unresponsive. Please refresh the page and try again.")
