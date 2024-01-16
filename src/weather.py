# src/weather.py
import random

def generate_weather(season):
    # Set temperature, wind, and rain ranges based on the season
    if season == "summer":
        temperature = random.randint(25, 35)
        wind = random.randint(5, 20)
        rain = random.randint(0, 20)
    elif season == "winter":
        temperature = random.randint(-5, 10)
        wind = random.randint(10, 30)
        rain = random.randint(20, 80)
    elif season == "spring":
        temperature = random.randint(15, 25)
        wind = random.randint(5, 15)
        rain = random.randint(10, 40)
    elif season == "fall":
        temperature = random.randint(10, 20)
        wind = random.randint(10, 25)
        rain = random.randint(20, 60)
    else:
        temperature = random.randint(15, 25)
        wind = random.randint(5, 15)
        rain = random.randint(10, 30)

    # Determine a description based on the generated values
    description = "Clear skies" if rain < 20 else "Cloudy with showers"
    if temperature > 30:
        description = "Hot and sunny"
    elif temperature < 0:
        description = "Freezing and snowy"
    elif rain > 60:
        description = "Heavy rain"

    return temperature, wind, rain, description
