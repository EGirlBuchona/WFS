from weather import generate_weather, get_real_weather
from visualization import display_forecast
from utils import get_day_name

def generate_weekly_forecast(season=None, city=None):
    with open("weekly_forecast.txt", "w", encoding="utf-8") as file:
        if city:
            file.write(f"Weekly Real-Weather Forecast for {city.capitalize()}:\n\n")
            for day in range(7):
                day_name = get_day_name(day)
                temperature, wind, rain, description = get_real_weather(city)
                if temperature is not None:
                    display_forecast(day_name, temperature, wind, rain, description, file)
                else:
                    file.write(f"{day_name} | Data not available\n")
        else:
            file.write(f"Weekly Seasonal Forecast for {season.capitalize()}:\n\n")
            for day in range(7):
                day_name = get_day_name(day)
                temperature, wind, rain, description = generate_weather(season)
                display_forecast(day_name, temperature, wind, rain, description, file)

if __name__ == "__main__":
    mode = input("Choose mode (1 for Real-Weather, 2 for Seasonal Simulation): ").strip()
    if mode == "1":
        city = input("Enter the city name for real weather data: ").strip()
        generate_weekly_forecast(city=city)
    elif mode == "2":
        season = input("Enter the season (summer, winter, spring, fall): ").strip().lower()
        generate_weekly_forecast(season=season)
    else:
        print("Invalid choice. Please enter 1 or 2.")
