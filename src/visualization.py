# src/visualization.py

def display_forecast(day, temperature, wind, rain):
    # Visualize wind level with bars and rain percentage with symbols
    wind_level = "🌬️" * (wind // 10)  # Each '🌬️' represents a level of wind intensity
    rain_level = "💧" * (rain // 20)  # Each '💧' represents 20% chance of rain

    # Display the formatted forecast
    forecast = f"{day} | Temp: {temperature}°C | Wind: {wind_level} | Rain: {rain_level}"
    print(forecast)
