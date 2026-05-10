import requests

def get_coordinates(city):
    cities = {
        "pune": (18.52, 73.85),
        "mumbai": (19.07, 72.88),
        "delhi": (28.61, 77.20),
        "bangalore": (12.97, 77.59)
    }
    return cities.get(city.lower(), (18.52, 73.85))


def fetch_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&current_weather=true&timezone=auto"
    
    response = requests.get(url)
    return response.json()