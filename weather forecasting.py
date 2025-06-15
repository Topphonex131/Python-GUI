# Import requests to fetch weather data from the internet
import requests

# Ask the user for the city name
city = input("Enter a city name to get weather: ")

# Replace with your own API key from OpenWeatherMap
api_key = "260d246f1e1cc4dbd6add73245a46b25"

# Build the URL to request weather info
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Send a GET request to the URL
response = requests.get(url)

# Convert the response into JSON format (dictionary)
data = response.json()

# Check if city was found (code 200 = OK)
if data["cod"] == 200:
    # Extract weather info
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    # Show the weather info
    print(f"\nWeather in {city.title()}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("\nCity not found. Please check the name and try again.")
