# src/visualization.py

def display_forecast(day, temperature, wind, rain, description, file=None):
    # Visualize wind level with symbols and rain percentage with icons
    wind_level = "🌬️" * (wind // 10)
    rain_level = "💧" * (rain // 20)

    # Choose an icon based on temperature
    if temperature > 30:
        weather_icon = "☀️"
    elif temperature < 0:
        weather_icon = "❄️"
    elif rain > 60:
        weather_icon = "🌧️"
    else:
        weather_icon = "⛅"

    # Create the forecast line
    forecast = f"{day} | {weather_icon} {temperature}°C | Wind: {wind_level} | Rain: {rain_level} | {description}"
    
    # Print to console
    print(forecast)

    # Save to file if specified
    if file:
        file.write(forecast + "\n")
