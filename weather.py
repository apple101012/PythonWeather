import requests

# APIs that were used: https://open-meteo.com/ and https://nominatim.org/release-docs/develop/api/Search/

location = input("Input your location: ")

locationurl = "https://nominatim.openstreetmap.org/search"
params1 = {
    "q" : "Levittown",
    "addressdetails" : 1,
    "format" : "json"
}
headers = {
    "User-Agent": "Tester"  # Necessary for the API can be anything
}

address_response = requests.get(locationurl, headers=headers, params=params1)
data1 = address_response.json()
display_name = data1[0].get("display_name")
lat = data1[0].get("lat")
long = data1[0].get("lon")

print(f"Name: {display_name}, Latitude: {lat}, Longitude: {long}")


url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": lat,
    "longitude": long,
    "temperature_unit": "fahrenheit",
    "wind_speed_unit": "mph",
    "precipitation_unit": "inch",
    "timezone": "America/New_York",
    "current": "temperature_2m",
    "daily" : "temperature_2m_max,temperature_2m_min"
}
payload = {}
headers = {}

response = requests.get(url, params=params)

if response.status_code != 200:
    print(f"Failed response code: {response.status_code}")
else:
    data = response.json()
    print("API Response:", data)  #print response

    current_data = data.get("current")
    temperature = current_data.get("temperature_2m")
    print(f"Current temp is: {temperature} F")

    daily_data = data.get("daily")
    max = 0
    max_data = daily_data.get("temperature_2m_max")
    for i in max_data:
        if(max < i):
            max = i
    print(f"Max temperature is {max}")


