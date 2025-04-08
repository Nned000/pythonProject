from tkinter import *

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
    print("1 USD це -", value)
    print(type(value))

def calculation():
    uah = int(entry1.get())
    x = uah / value
    y = round(x, 2)
    label2["text"] = y, "USD"

def click_ent(event):
    entry1.delete(0, END)

root = Tk()
root.geometry("300x300")
root.title("Convertor")

label1 = Label(text = "Конвертор валют", fg = "red", font = "Arial 18")
label1.pack()

entry1 = Entry()
entry1.pack(pady = 20)
entry1.insert(0, "Введіть суму у UAH")

button1 = Button(text = "Конвертувати", bg="blue", fg = "white", command = calculation)
button1.pack(pady =3)

label2 = Label(font = "Arial 18", fg = "red")
label2.pack(pady = 10)

entry1.bind("<Button-1>", click_ent)

root.mainloop()