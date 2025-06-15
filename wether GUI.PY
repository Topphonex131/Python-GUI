import requests
import tkinter as tk
from tkinter import messagebox

# Replace this with your real OpenWeatherMap API key
API_KEY = "260d246f1e1cc4dbd6add73245a46b25"

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = f"Weather in {city.title()}:\n\nTemperature: {temp}°C\nDescription: {desc}\nHumidity: {humidity}%\nWind Speed: {wind} m/s"
        result_label.config(text=result)
    else:
        messagebox.showerror("City Not Found", f"Could not find city: {city}")

# Create the main window
root = tk.Tk()
root.title("Simple Weather App")
root.geometry("400x300")
root.config(bg="#dfe6e9")

# City entry
city_entry = tk.Entry(root, width=30, font=("Arial", 14))
city_entry.pack(pady=20)

# Get weather button
get_button = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12), bg="#0984e3", fg="white")
get_button.pack(pady=10)

# Label to show the result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#dfe6e9", justify="left")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
