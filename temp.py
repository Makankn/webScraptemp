from bs4 import BeautifulSoup
import requests


url = 'https://www.scrapethissite.com/pages/simple/'

r=requests.get(url)
soup=BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())