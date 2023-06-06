""""
1 - presentation layer (cli interface, show table). 
2 - data acces layer (database interaction, web interaction) DAO -> Adapter / Gateway - provide pradigm to incapsulate
interaction with 3rd-party system in our code.
3 - business_loginc layer (sorting, group of data).
"""

import requests
from prettytable import PrettyTable


if __name__ == "__main__":
    while True:
        user_choice = input("1 - Check weather\n2 - Exit\nYour choice: ")
        if user_choice == '2':
            print("GOODBYE!")
            break
        elif user_choice == '1':
            answer = input("Enter cities: ")
            cities = answer.split()
            table = PrettyTable()
            with requests.Session() as session:
                for city in cities:
                    resp = session.request("GET", f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ea07328167d6ff9870fe5ed517c6c113&units=metric")
                    weather_data = resp.json()
                    print(weather_data)
                    city_name = weather_data['name']
                    temp = weather_data['main']['temp']
                    description = weather_data['weather'][0]['description']
                    humidity = weather_data['main']['humidity']

                    table.field_names = ['city', 'temp', 'description', 'humidity']
                    table.add_row([city_name, temp, description, humidity])
                
                print(table)
