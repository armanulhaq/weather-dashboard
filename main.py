import streamlit as st
import plotly.express as px

st.header("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forcasted days")
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2024-09-30", "2024-10-01", "2024-10-02"]
temperatures = [23, 28, 21]

figure = px.line(x=dates, y=temperatures, labels={"x":"Date", "y":"Temperature in C"})  #Creates a line graph
st.plotly_chart(figure)
