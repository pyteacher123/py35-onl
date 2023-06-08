from __future__ import annotations
from .utils import show_as_table
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import WeatherServiceProtocol


class CliApp:
    def __init__(self, weather_service: WeatherServiceProtocol) -> None:
        self._weather_service = weather_service

    def run(self) -> None:
        while True:
            user_choice = input("1 - Check weather\n2 - Exit\nYour choice: ")
            if user_choice == '2':
                print("GOODBYE!")
                break
            elif user_choice == '1':
                answer = input("Enter cities: ")
                weather_data_in_cities = self._weather_service.get_weather_in_cities(cities=answer)
                show_as_table(weather_data_in_cities)
