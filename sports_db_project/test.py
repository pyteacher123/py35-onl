import sqlite3


connection = sqlite3.connect('sports.db')
cursor = connection.cursor()
country = input('Enter country name: ')

res = cursor.execute('SELECT * FROM countries WHERE name = ?;', (country, ))
print(res.fetchall())
