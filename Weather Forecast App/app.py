import requests

def get_weather(city):
    api_key = "**************"  # Replace with your actual OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Check the response from the API
    print(data)  # This will show you the structure of the response

    if data.get("cod") != 200:  # Check for a successful response
        print(f"Error: {data.get('message', 'City not found!')}")
    else:
        main = data["main"]
        weather = data["weather"][0]["description"]
        temp_celsius = main['temp'] - 273.15  # Convert temperature from Kelvin to Celsius
        print(f"Weather in {city}: {weather}, Temp: {temp_celsius:.2f}°C")

# Taking user input for the city
city = input("Enter the city name to get the weather: ")

# Calling the function with the user input
get_weather(city)
