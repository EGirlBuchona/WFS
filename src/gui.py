import tkinter as tk
from tkinter import messagebox
from weather import get_real_weather, generate_weather
from utils import get_day_name

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast Simulator")
        self.root.geometry("500x400")

        # Title Label
        self.label_title = tk.Label(root, text="Weather Forecast Simulator", font=("Arial", 16))
        self.label_title.pack(pady=10)

        # Mode Selection
        self.mode_var = tk.StringVar(value="real")
        self.radio_real = tk.Radiobutton(root, text="Real-Weather", variable=self.mode_var, value="real")
        self.radio_simulation = tk.Radiobutton(root, text="Seasonal Simulation", variable=self.mode_var, value="simulation")
        self.radio_real.pack()
        self.radio_simulation.pack()

        # City/Season Input
        self.label_input = tk.Label(root, text="Enter city (for real weather) or season (summer, winter, spring, fall):")
        self.label_input.pack(pady=5)
        self.entry_input = tk.Entry(root, width=30)
        self.entry_input.pack()

        # Forecast Display
        self.text_display = tk.Text(root, height=10, width=50)
        self.text_display.pack(pady=10)

        # Get Forecast Button
        self.button_get_forecast = tk.Button(root, text="Get Forecast", command=self.get_forecast)
        self.button_get_forecast.pack(pady=5)

    def get_forecast(self):
        self.text_display.delete(1.0, tk.END)  # Clear previous forecast
        mode = self.mode_var.get()
        user_input = self.entry_input.get().strip()

        if mode == "real":
            self.get_real_weather_forecast(user_input)
        elif mode == "simulation":
            self.get_simulated_forecast(user_input)
        else:
            messagebox.showerror("Error", "Please select a mode.")

    def get_real_weather_forecast(self, city):
        if not city:
            messagebox.showerror("Input Error", "Please enter a city name.")
            return

        self.text_display.insert(tk.END, f"Weekly Real-Weather Forecast for {city.capitalize()}:\n\n")
        for day in range(7):
            day_name = get_day_name(day)
            temperature, wind, rain, description = get_real_weather(city)
            if temperature is not None:
                forecast = f"{day_name} | {temperature}°C | Wind: {wind} m/s | Rain: {rain} mm | {description}\n"
                self.text_display.insert(tk.END, forecast)
            else:
                self.text_display.insert(tk.END, f"{day_name} | Data not available\n")

    def get_simulated_forecast(self, season):
        if season not in ["summer", "winter", "spring", "fall"]:
            messagebox.showerror("Input Error", "Please enter a valid season (summer, winter, spring, fall).")
            return

        self.text_display.insert(tk.END, f"Weekly Seasonal Forecast for {season.capitalize()}:\n\n")
        for day in range(7):
            day_name = get_day_name(day)
            temperature, wind, rain, description = generate_weather(season)
            forecast = f"{day_name} | {temperature}°C | Wind: {wind} km/h | Rain: {rain} mm | {description}\n"
            self.text_display.insert(tk.END, forecast)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
