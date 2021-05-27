from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.doordash.com/store/yafo-kitchen-charlotte-63003')

soup = BeautifulSoup(source.content, 'html.parser')
print(soup)