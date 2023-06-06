from dataclasses import dataclass
from typing import Optional


@dataclass
class Coord:
    lon: float
    lat: float


@dataclass
class WeatherInfo:
    id: int
    main: str
    description: str
    icon: str


@dataclass
class MainInfo:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


@dataclass
class WindInfo:
    speed: float
    deg: int
    gust: float


@dataclass
class CloudInfo:
    all: int


@dataclass
class SysInfo:
    type: Optional[int]
    id: Optional[int]
    country: str
    sunrise: int
    sunset: int


@dataclass
class WeatherDTO:
    coord: Coord
    weather: list[WeatherInfo]
    base: str
    main: MainInfo
    visibility: int
    wind: WindInfo
    clouds: CloudInfo
    dt: int
    sys: SysInfo
    timezone: int
    id: int
    name: str
    cod: int
    message: Optional[str]
