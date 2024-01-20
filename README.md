# Weather Forecast Simulator

**Date Created:** January 15, 2024  
**Author:** Gustavo Cocone Zavaleta

## Overview

The **Weather Forecast Simulator** is a dynamic Python program that generates a 7-day weather forecast based on a selected season or retrieves real-time weather data from OpenWeather API for a specified city. The simulator provides detailed daily weather conditions, including temperature, wind, and rain probabilities, displayed in a user-friendly console with ASCII graphics and emoji icons.

Version 3 introduces real-world weather data integration using OpenWeather API, along with improved error handling and file encoding support for Unicode.

## Features

- **Real-Time Weather Data**: Fetches real-time weather data from OpenWeather API based on user-specified city.
- **Season-Based Forecasting**: Generates realistic daily weather data (temperature, wind, and rain) based on the selected season: summer, winter, spring, or fall.
- **Detailed Daily Weather**: Each day in the forecast includes:
  - Temperature in Celsius
  - Wind intensity displayed visually with ASCII bars
  - Rain probability represented with icons and percentages
  - Descriptive weather phrases, such as "Clear skies" or "Heavy rain"
- **Console Visualization with Icons**: Uses emoji icons (e.g., ☀️ for sunny, 🌧️ for rain) to visually represent weather conditions, enhancing readability.
- **Forecast Logging**: Saves each 7-day forecast to a text file (`weekly_forecast.txt`) for easy reference and record-keeping.
- **Modular Design**: The code is organized into separate modules for weather generation, visualization, and utilities, allowing easy updates and expansions.

## File Structure

```plaintext
WFS/
├── data/                        # Placeholder for potential data files
│   ├── seasons.json             # Information on weather ranges per season (future use)
│   └── icons.txt                # Optional ASCII icons for weather representation
├── src/                         # Source code
│   ├── main.py                  # Main script to execute the forecast
│   ├── weather.py               # Generates weather data with descriptions and API integration
│   ├── visualization.py         # Handles display formatting and file output
│   └── utils.py                 # Utility functions (e.g., date management)
├── tests/                       # Placeholder for testing scripts
│   └── test_weather.py          # Tests for weather generation
├── README.md                    # Project documentation
├── requirements.txt             # List of dependencies (if any)
└── .gitignore                   # Specifies files to ignore in Git
```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/EGirlBuchona/WFS.git
   cd WFS
   ```

2. **Install Dependencies**:  
   Ensure Python 3.6 or later is installed. Install required packages with:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Program**:
   ```bash
   python src/main.py
   ```

4. **Choose Mode**:
   - **Real-Weather Mode**: Enter a city name (e.g., "Tokyo") to retrieve real-time data from OpenWeather.
   - **Seasonal Simulation**: Enter a season (e.g., "summer") to generate simulated weather data.

## Example Usage

Upon running the program, you’ll be prompted to choose a mode. After selecting one, you will see a 7-day weather forecast in the console, similar to this:

```plaintext
Weekly Real-Weather Forecast for London:

Monday    | ☀️  32°C | Wind: 🌬️🌬️ | Rain: 💧 | Hot and sunny
Tuesday   | ⛅  29°C | Wind: 🌬️🌬️🌬️ | Rain:  | Clear skies
Wednesday | 🌧️ 24°C | Wind: 🌬️🌬️🌬️ | Rain: 💧💧 | Cloudy with showers
...
```

The forecast is saved to `weekly_forecast.txt` in the project directory, with each day’s conditions for easy review.

**Date Updated:** January 19, 2024

## New in Version 3

- **Real-Time Weather Data**: Fetches real-time weather data from OpenWeather API based on user input.
- **Improved Error Handling**: Enhanced error messages for API failures and connection issues.
- **Unicode Support**: File output now supports UTF-8 encoding to handle Unicode characters (e.g., emojis).

## Future Improvements

- **Add a GUI**: Create a graphical interface using `tkinter` or `PyQt` for an enhanced user experience.
- **Extended Forecast Options**: Allow users to specify a custom date range for the forecast.
- **Graphical Representation**: Integrate `matplotlib` for temperature and wind graphs.

## License

This project is open-source under the MIT License.

## Author’s Note

This project is part of a series of professional portfolio projects by Gustavo Cocone Zavaleta. Thank you for reviewing the work!

