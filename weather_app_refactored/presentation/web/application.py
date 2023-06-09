import requests
from data_access.openWeatherMap.client import OpenWeatherMap
from business_logic.services import GetWeatherService
from config import OWM_API_KEY, OWM_BASE_URL
from .server import Request, Response


def get_weather_controller(request: Request) -> Response:
    cities = request.params.get('query')[0]
    with requests.Session() as session:
        weather_api = OpenWeatherMap(session=session, api_key=OWM_API_KEY, base_url=OWM_BASE_URL)
        weather_service = GetWeatherService(weather_api_adapter=weather_api)
        weather_data_in_cities = weather_service.get_weather_in_cities(cities=cities)
    
        headers = {"Content-Type": "text/html"}
        mes = "<html><body><h1><b>Weather Data Table</b></h1><table>"
        mes += "<tr><th>city</th><th>temp</th><th>description</th><th>humidity</th></tr>"
        for weather_data in weather_data_in_cities:
            mes += (f"<tr><td>{weather_data.name}</td><td>{weather_data.main.temp}</td>"
                    f"<td>{weather_data.weather[0].description}</td><td>{weather_data.main.humidity}</td></tr>")
        mes += "</table></body></html>"
        return Response(
            status="200 OK",
            headers=headers,
            body=mes
        )


def hello_world_controller(request: Request) -> Response:
    mes = "<h1>Hello World!</h1>"
    headers = {"Content-Type": "text/html"}
    return Response(
        status="200 OK",
        headers=headers,
        body=mes
    )


urlpatterns = [
    ('/', get_weather_controller),
    ('/hello', hello_world_controller)
]


class WebApplication:  # Web-Frameworks: Django, Flask, FastAPI
    def _get_404_error(self, request: Request) -> Response:
        mes = f"<h1>404 ERROR, URL {request.path} NOT FOUND"
        headers = {"Content-Type": "text/html"}
        return Response(
            status="404 NOT FOUND",
            headers=headers,
            body=mes
        )

    def __call__(self, request: Request) -> Response:
        for url_path, controller in urlpatterns:
            if url_path == request.path:
                resp = controller(request)
                return resp
        
        return self._get_404_error(request=request)
