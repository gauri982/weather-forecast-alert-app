import requests

def get_coordinates(city):
    # Simple fixed mapping (for project simulation)
    locations = {
        "pune": (18.52, 73.85),
        "mumbai": (19.07, 72.88),
        "delhi": (28.61, 77.20),
        "bangalore": (12.97, 77.59)
    }
    return locations.get(city.lower(), (18.52, 73.85))  # default Pune


def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Error fetching weather data")
        return None

    return response.json()


def analyze_weather(data):
    weather = data["current_weather"]

    temp = weather["temperature"]
    wind = weather["windspeed"]

    alerts = []

    if temp > 40:
        alerts.append("🔥 Heat Wave Alert")
    if temp < 10:
        alerts.append("❄️ Cold Weather Alert")
    if wind > 50:
        alerts.append("🌪️ Storm/Wind Alert")

    return temp, wind, alerts


def main():
    city = input("Enter city name: ")

    lat, lon = get_coordinates(city)

    data = get_weather(lat, lon)

    if not data:
        return

    temp, wind, alerts = analyze_weather(data)

    print("\n🌍 WEATHER REPORT")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Wind Speed:", wind, "km/h")

    print("\n⚠️ ALERTS:")
    if alerts:
        for a in alerts:
            print("-", a)
    else:
        print("✅ No alerts - Normal weather")


if __name__ == "__main__":
    main()