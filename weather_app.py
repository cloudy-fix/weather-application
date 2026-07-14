import os

import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


class WeatherApp(App):
    def build(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")

        layout = BoxLayout(orientation="vertical", padding=12, spacing=10)

        self.city_input = TextInput(hint_text="Enter city name", multiline=False)
        layout.add_widget(self.city_input)

        self.result_label = Label(text="Weather details will appear here")
        layout.add_widget(self.result_label)

        get_weather_button = Button(text="Get Weather")
        get_weather_button.bind(on_press=self.get_weather)
        layout.add_widget(get_weather_button)

        return layout

    def get_weather(self, _instance):
        if not self.api_key:
            self.result_label.text = "Set OPENWEATHER_API_KEY before running the app."
            return

        city_name = self.city_input.text.strip()
        if not city_name:
            self.result_label.text = "Please enter a city name."
            return

        try:
            response = requests.get(
                OPENWEATHER_BASE_URL,
                params={"q": city_name, "appid": self.api_key, "units": "metric"},
                timeout=10,
            )
            weather_data = response.json()
        except requests.RequestException as exc:
            self.result_label.text = f"Network error: {exc}"
            return

        if response.status_code != 200:
            message = weather_data.get("message", "Could not retrieve weather data.")
            self.result_label.text = f"Error: {message} (HTTP {response.status_code})"
            return

        main_data = weather_data.get("main", {})
        weather = weather_data.get("weather", [{}])[0]
        wind_data = weather_data.get("wind", {})

        self.result_label.text = (
            f"Temperature: {main_data.get('temp', 'N/A')} C\n"
            f"Weather: {weather.get('description', 'N/A').capitalize()}\n"
            f"Humidity: {main_data.get('humidity', 'N/A')}%\n"
            f"Wind Speed: {wind_data.get('speed', 'N/A')} m/s\n"
            f"Pressure: {main_data.get('pressure', 'N/A')} hPa"
        )


if __name__ == "__main__":
    WeatherApp().run()

