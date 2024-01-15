# Weather Forecast Simulator

**Date Created:** January 15, 2024  
**Author:** Gustavo Cocone Zavaleta

## Overview

The **Weather Forecast Simulator** is a simple yet dynamic Python program that generates a 7-day weather forecast. This forecast simulates daily weather conditions based on the selected season, providing temperature, wind, and rain probabilities. The program is designed to be expandable, with options for ASCII visuals and descriptive outputs that enhance readability.

## Features

- **Season-Based Forecasting**: Generates realistic daily weather data (temperature, wind, and rain) that varies based on the selected season: summer, winter, spring, or fall.
- **Daily Weather Details**: Each day in the forecast includes:
  - Temperature in Celsius
  - Wind intensity displayed visually with ASCII bars
  - Rain probability represented as a percentage
- **Console Visualization**: Displays the forecast in the console in an easy-to-read format.
- **Modular Design**: The code is organized into functions and modules to allow easy updates and expansions.

## File Structure

```plaintext
weather_forecast_simulator/
├── data/                        # Placeholder for potential data files
│   ├── seasons.json             # Information on weather ranges per season (future use)
│   └── icons.txt                # Optional ASCII icons for weather representation
├── src/                         # Source code
│   ├── main.py                  # Main script to execute the forecast
│   ├── weather.py               # Generates weather data
│   ├── visualization.py         # Handles display formatting
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
   git clone https://github.com/your-username/weather_forecast_simulator.git
   cd weather_forecast_simulator
   ```

2. **Install Dependencies**:  
   This project requires Python 3.6 or later. All dependencies are standard libraries, so there is no need to install additional packages. You can still run:
   ```bash
   pip install -r requirements.txt
   ```
   to check for any future dependencies.

3. **Run the Program**:
   ```bash
   python src/main.py
   ```

4. **Enter the Season** when prompted to see a forecast tailored for that season.

## Example Usage

Upon running the program, you’ll be prompted to enter a season. After selecting one, you will see a 7-day weather forecast in the console, similar to this:

```plaintext
Weather Forecast for Summer:

Monday | 🌞 29°C | Wind: ||| | Rain: 💧💧 | Clear skies
Tuesday | ⛅ 31°C | Wind: |||| | Rain: 💧 | Hot and sunny
...
```

## Future Improvements

- **Weather Descriptions**: Descriptive phrases for weather conditions, such as “Hot and sunny” or “Freezing and snowy.”
- **Weather Icons**: Emoji icons to represent various conditions visually (e.g., ☀️ for sunny, 🌧️ for rain).
- **File Output**: Option to save forecasts to a file for easy reference.
  
## License

This project is open-source under the MIT License.

## Author’s Note

This project is a series of professional portfolio projects by Gustavo Cocone Zavaleta. Thank you for reviewing the work!
