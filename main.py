# selenium -> actions on browser
# bs4 -> better for scraping

from bs4 import BeautifulSoup
from Selenium import 
import requests


def get_currency(in_curr, out_curr):
    url = f"https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate_str = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate_str.split(" ")[0])
    return rate


# print(get_currency("USD", "INR"))

def get_curr_list():
  url = "https://www.x-rates.com/"
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  list_ul = soup.select("#from_scroller")
  print(list_ul)

get_curr_list()