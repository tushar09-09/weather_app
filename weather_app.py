import requests

API_KEY = "837bf956dd2e6fc835e30453222e953d"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}  # Fetch in Celsius
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_condition = data["weather"][0]["description"].title()
        wind_speed = data["wind"]["speed"]

        # Display weather report
        print(f"\n🌍 Weather in {city_name}, {country}:")
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌥️ Condition: {weather_condition}")
        print(f"💨 Wind Speed: {wind_speed} m/s")

    else:
        print("❌ Error: City not found or API issue. Please check your input.")


def main():
    print("🌦️ Welcome to the Basic Weather App 🌦️")
    city = input("Enter a city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("❌ Error: Please enter a valid city name.")


if __name__ == "__main__":
    main()
