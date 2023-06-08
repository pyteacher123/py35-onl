from __future__ import annotations
from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from data_access.openWeatherMap.dto import WeatherDTO


class WeatherApiAdapterProtocol(Protocol):
    def get_current_weather_in_city(self, city_name: str) -> WeatherDTO:
        raise NotImplementedError


class WeatherServiceProtocol(Protocol):
    def get_weather_in_cities(self, cities: str) -> list[WeatherDTO]:
        raise NotImplementedError
