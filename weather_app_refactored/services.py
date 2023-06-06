from __future__ import annotations
from openWeatherMap.dto import WeatherDTO
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from interfaces import WeatherApiAdapterProtocol


class GetWeatherService:
    def __init__(self, weather_api_adapter: WeatherApiAdapterProtocol) -> None:
        self._weather_api = weather_api_adapter
    
    def get_weather_in_cities(self, cities: str) -> list[WeatherDTO]:
        cities = cities.split()
        result: list[WeatherDTO] = []
        for city in cities:
            weather_data = self._weather_api.get_current_weather_in_city(city_name=city)
            result.append(weather_data)

        result.sort(key=lambda x: x.main.temp, reverse=True)

        return result
