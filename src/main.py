# src/main.py
from weather import generate_weather
from visualization import display_forecast
from utils import get_day_name

def generate_weekly_forecast(season):
    # Generate and display the forecast for each day of the week
    for day in range(7):
        day_name = get_day_name(day)
        temperature, wind, rain = generate_weather(season)
        display_forecast(day_name, temperature, wind, rain)

if __name__ == "__main__":
    season = input("Enter the season (summer, winter, spring, fall): ").strip().lower()
    print(f"Weather Forecast for {season.capitalize()}:\n")
    generate_weekly_forecast(season)
