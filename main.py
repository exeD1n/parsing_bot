from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable
from time import sleep


mytable = PrettyTable()
mytable.field_names = ["Name", "Cost"]

for page in range(1,100):
    
    sleep(3)
    url = f"https://steamcommunity.com/market/search?appid=730#p{page}_popular_desc"
    response = requests.get(url) #Запрос к сайту
    soup = BeautifulSoup(response.text, "lxml") #Передает в BeautifulSoup код html 'response.text'

    data = soup.find_all("a", class_="market_listing_row_link")
    
    for i in data:
        name = i.find("span", class_="market_listing_item_name").text #Получение имени товара

        price = (i.find("span", class_="market_table_value normal_price")).find("span", class_="normal_price").text #Получение цены товара
        cost = float((price.split(' ')[0]).split('$')[1])
        mytable.add_row([name, round((cost*77.12), 2)+1.0])

print(mytable)