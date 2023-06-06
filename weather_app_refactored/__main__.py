""""
1 - presentation layer (cli interface, show table). 
2 - data acces layer (database interaction, web interaction) DAO -> Adapter / Gateway - provide pradigm to incapsulate
interaction with 3rd-party system in our code.
3 - business_loginc layer (sorting, group of data).
"""

import requests
from prettytable import PrettyTable
from openWeatherMap.client import OpenWeatherMap
from services import GetWeatherService


if __name__ == "__main__":
    while True:
        user_choice = input("1 - Check weather\n2 - Exit\nYour choice: ")
        if user_choice == '2':
            print("GOODBYE!")
            break
        elif user_choice == '1':
            answer = input("Enter cities: ")
            table = PrettyTable()
            table.field_names = ['city', 'temp', 'description', 'humidity']
            with requests.Session() as session:
                weather_api = OpenWeatherMap(session=session)
                weather_service = GetWeatherService(weather_api_adapter=weather_api)
                data = weather_service.get_weather_in_cities(cities=answer)
                
            for weather_data in data:            
                table.add_row([weather_data.name, weather_data.main.temp, weather_data.weather[0].description, 
                                        weather_data.main.humidity])
                
            print(table)
