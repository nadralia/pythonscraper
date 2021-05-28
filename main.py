from bs4 import BeautifulSoup
import requests
import csv

BASE_URL = 'https://identity.doordash.com'
URL = 'https://www.doordash.com/store/yafo-kitchen-charlotte-63003'
LOGIN_ROUTE = '/auth'

HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
'origin':BASE_URL, 'referer': BASE_URL + LOGIN_ROUTE}

s = requests.session()

# csrf_token = s.get(BASE_URL).cookies['csrftoken']

csrf_token = s.get(BASE_URL)

login_payload = {
    'clientId': "1666519390426295040",
    'deviceId': '',
    'password': "n4355342551`457314",
    'redirectUri': "https://www.doordash.com/post-login/",
    'responseType': "code",
    'scope': "*",
    'state': "/home/||5846e291-8591-427d-8c92-f8352b04e225",
    'username': "test@gmail.com",
    'csrfmiddlewaretoken': csrf_token,
}

login_req = s.post(BASE_URL + LOGIN_ROUTE, headers=HEADERS, data=login_payload)
print('--*******-LoginResponse-********---',login_req)

source = requests.get(URL).text

soup = BeautifulSoup(source, 'html5lib') 


csv_file = open('web_scraper_data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Category", "Item Name", "Description Price",	"Option Name", "Choice", "Choice Price"])


for menus in soup.find_all('div'):
    csv_writer.writerow([menus])
    print('--*******-H1Body-********---', menus)

# print(soup.prettify())