import requests
from bs4 import BeautifulSoup



url = 'https://example.com'



response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all('h1')
for title in titles:
    print(title.get_text())


