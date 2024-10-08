import requests

API_key = "e5851c77c3b81944f9ab798ff19622d2"

def get_data(place, forecast_days=None, option=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    #len(filtered_data) = 40. Per day number of data = 24/3 (as 3 hrs report) = 8
    #which means 5 day data is given
    number_of_values_required = 8 * forecast_days
    filtered_data = filtered_data[:number_of_values_required]
    return filtered_data
