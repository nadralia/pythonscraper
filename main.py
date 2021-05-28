from bs4 import BeautifulSoup
import requests
import csv


URL = 'https://www.doordash.com/store/yafo-kitchen-charlotte-63003'

source = requests.get(URL).text

soup = BeautifulSoup(source, 'html5lib') 


csv_file = open('web_scraper_data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Category", "Item Name", "Description Price",	"Option Name", "Choice", "Choice Price"])


for menus in soup.find_all('h1'):
    csv_writer.writerow([menus])
    print(menus)

# print(soup.prettify())