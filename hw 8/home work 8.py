import sqlite3
import datetime
import time
from bs4 import BeautifulSoup
import requests


# створити базу даних
# connection = sqlite3.connect("weather_db.sl3", 5)
# cur = connection.cursor()
# cur.execute("CREATE TABLE weather_table (date DATE, temperature TEXT);")
# connection.commit()
# connection.close()

while True:
    response = requests.get("https://sinoptik.ua/pohoda/kyiv")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all(class_="R1ENpvZz")
        temp = soup_list[0]
        print("Weather now -", temp.text)

    connection = sqlite3.connect("weather_db.sl3", 5)
    cur = connection.cursor()
    cur.execute("INSERT INTO weather_table (date, temperature) VALUES (?, ?)",(datetime.datetime.now().isoformat(), temp.text))
    connection.commit()
    connection.close()
    time.sleep(1800)
