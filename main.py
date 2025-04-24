import requests
from colorama import Fore, Style

city_name = input("Enter the city name: ").title()
api_key = "YOUR_API_KEY"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"\nThe weather of {city_name} is: \n")
    print(f"Description: {data["weather"][0]["description"]}")
    print(f"Temperature: {data["main"]["temp"]}")
    print(f"Humidity: {data["main"]["humidity"]}")
    print(f"Wind speed: {data["wind"]["speed"]}")
else:
    print(Fore.RED + "City name not found or API error occurred!" + Style.RESET_ALL)