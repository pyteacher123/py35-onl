"""
DRY - don't repeat yourself.
"""
from __future__ import annotations
from dacite import from_dict

from config import OWM_BASE_URL, OWM_API_KEY
from .dto import WeatherDTO

from typing import TYPE_CHECKING, Any, Optional, TypeVar
if TYPE_CHECKING:
    from requests import Session, Response


T = TypeVar('T')


class OpenWeatherMap:
    def __init__(self, session: Session) -> None:
        self._session = session
    
    def _request(
            self,
            method: str,
            url_path: str,
            headers: Optional[dict[str, Any]] = None,
            params: Optional[dict[str, Any]]  = None,
            json = None,
            data = None
    ) -> Response:
        url = OWM_BASE_URL + url_path
        res = self._session.request(method=method, url=url, params=params, headers=headers, json=json, data=data)
        return res

    def _get(self, model: type[T], url_path: str, params: dict[str, Any]) -> T:
        resp = self._request("GET", url_path=url_path, params=params)
        return from_dict(model, resp.json())

    def get_current_weather_in_city(self, city_name: str) -> WeatherDTO:
        resp = self._get(WeatherDTO, url_path="data/2.5/weather", params={"q": city_name, "appid": OWM_API_KEY, "units": "metric"})
        return resp
