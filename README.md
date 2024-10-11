# Weather Forecast Application

## Description
The Weather Forecast Application is a web app built with Streamlit that allows users to retrieve and visualize weather forecasts for a specified location. By utilizing the OpenWeatherMap API, users can select a place and the number of forecast days (up to 5) to view temperature trends or sky conditions.

## Features
- User-friendly interface for entering location and selecting forecast days.
- Visualization of temperature data as line graphs.
- Display of sky conditions with corresponding images.
- Error handling for invalid locations and connection issues.

## Technologies Used
- Python
- Streamlit
- Plotly Express
- OpenWeatherMap API

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/weather-forecast-app.git
   cd weather-forecast-app
```
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3. Install the required packages:
```bash
pip install streamlit plotly requests
```
4. Obtain an API key from OpenWeatherMap and replace API_key in the code:
```bash
API_key = "your_api_key_here"
```
5. Run the application:
```bash
streamlit run app.py
