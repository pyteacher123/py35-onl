from __future__ import annotations
from prettytable import PrettyTable
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.openWeatherMap.dto import WeatherDTO


def show_as_table(data: list[WeatherDTO]) -> None:
    table = PrettyTable()
    table.field_names = ('city', 'temp', 'description', 'humidity')
    for weather_data in data:
        table.add_row([
            weather_data.name, 
            weather_data.main.temp, 
            weather_data.weather[0].description, 
            weather_data.main.humidity]
        )  
    print(table)
