from bs4 import BeautifulSoup
import requests
response = requests.get("https://minfin.com.ua/ua/currency/converter/?converter-type=bestbank&from=usd&to=uah&val1=1&val2=41.25")
if response.status_code == 200:
    print("Конвертор валют з UAH в USD")
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all(class_="zlkj5-1 cNCStF")
    value_in_class = soup.find_all("input", {'class':'zlkj5-1 cNCStF'})
    value_uah = value_in_class[1]['value']
    value = float(value_uah)
    print("1 USD це -", value, "UAH")
    print(type(value))

class Convert:
    def __init__(self):
        uah = int(input("Впишість кількість UAH - "))
        x = uah / value
        print(round(x, 2), "USD")

start_con = Convert()

