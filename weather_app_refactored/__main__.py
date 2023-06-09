""""
1 - presentation layer (cli interface, show table) | (web interface (html), web server). 
2 - data acces layer (database interaction, web interaction) DAO -> Adapter / Gateway - provide pradigm to incapsulate
interaction with 3rd-party system in our code.
3 - business_loginc layer (sorting, group of data).
"""

import sys
import requests

from data_access.openWeatherMap.client import OpenWeatherMap
from business_logic.services import GetWeatherService
from presentation.cli.app import CliApp
from config import OWM_API_KEY, OWM_BASE_URL, SERVER_HOST, SERVER_PORT
from presentation.web.server import HttpServer, HttpRequestHandler
from presentation.web.application import WebApplication


def run_cli():
    with requests.Session() as session:
        # creation of adapter (it incapsulates all interaction with 3rd-party data sources)
        weather_api = OpenWeatherMap(session=session, api_key=OWM_API_KEY, base_url=OWM_BASE_URL)
        # creation of service (it incapsulates all the code that realize the business rules of our application)
        weather_service = GetWeatherService(weather_api_adapter=weather_api)
        # creation of app (it incapsulates all interaction with the users of our application)
        app = CliApp(weather_service=weather_service)
        app.run()


def run_web():
    application = WebApplication()
    server = HttpServer(
        server_address=(SERVER_HOST, SERVER_PORT),
        RequestHandlerClass=HttpRequestHandler
    )
    server.set_app(application)
    server.serve_forever()


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == 'cli':
        run_cli()
    elif mode == 'web':
        run_web()
