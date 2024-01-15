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

    return temperature, wind, rain
