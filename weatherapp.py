import requests
from datetime import datetime

api_key = 'be491c4f9c475948b301848772f7e50c'

while True:
    user_city = input("Enter your city: ")
    if user_city.lower() == "quit":
        break
    weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_city}&units=imperial&appid={api_key}")
    if weather_info.status_code != 200:
        print(f"City not found. Please enter a valid city name.")
        continue

    weather_data = weather_info.json()

    # Extract the temperature in degrees Fahrenheit
    temp_fahrenheit = weather_data['main']['temp']

    # Convert the temperature to degrees Celsius
    temp_celsius = (temp_fahrenheit - 32) * 5/9

    # Get thew current day
    today = datetime.now().strftime('%A')

    # Print the temperature in degrees Celsius with floating-point numberdisplayed with two decimal places
    print(f"Temperature in {user_city} on {today}: {temp_celsius:.2f}°C")
