# Weather Forecast Simulator

**Date Created:** January 15, 2024  
**Author:** Gustavo Cocone Zavaleta

## Overview

The **Weather Forecast Simulator** is a dynamic Python program that generates a 7-day weather forecast based on a selected season. The simulator provides detailed daily weather conditions, including temperature, wind, and rain probabilities. With a user-friendly console visualization, ASCII graphics, and emoji icons, this tool offers an engaging way to display forecast information. Version 2 introduces detailed weather descriptions, emoji icons for enhanced visualization, and a feature to save forecasts to a file.

## Features

- **Season-Based Forecasting**: Generates realistic daily weather data (temperature, wind, and rain) that varies based on the selected season: summer, winter, spring, or fall.
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
│   ├── weather.py               # Generates weather data with descriptions
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
   This project requires Python 3.6 or later. All dependencies are standard libraries, so no additional packages are needed. You can still run:
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

Monday    | ☀️  32°C | Wind: 🌬️🌬️ | Rain: 💧 | Hot and sunny
Tuesday   | ⛅  29°C | Wind: 🌬️🌬️🌬️ | Rain:  | Clear skies
Wednesday | 🌧️ 24°C | Wind: 🌬️🌬️🌬️ | Rain: 💧💧 | Cloudy with showers
...
```

The forecast will also be saved to `weekly_forecast.txt` in the project directory, with each day’s conditions for easy review.

**Date Updated:** January 18, 2024
## New in Version 2

- **Weather Descriptions**: Detailed descriptions based on temperature, wind, and rain levels, such as “Hot and sunny” or “Cloudy with showers.”
- **Emoji Icons**: Visual representation of weather conditions using icons like ☀️, 🌧️, and ❄️.
- **File Output**: Each forecast is saved to a text file (`weekly_forecast.txt`) for future reference.

## Future Improvements

- **Add a GUI**: Create a graphical interface using `tkinter` or `PyQt` for an enhanced user experience.
- **Real-World Data from APIs**: Integrate with a weather API (e.g., OpenWeatherMap) for real-time data comparison.
- **Forecast Accuracy Simulation**: Implement "confidence" levels for forecast accuracy.

## License

This project is open-source under the MIT License.

## Author’s Note

This project is part of a series of professional portfolio projects by Gustavo Cocone Zavaleta. Thank you for reviewing the work!
