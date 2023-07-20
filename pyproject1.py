import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.hopkinsmedicine.org/profiles/search?query=')
soup = BeautifulSoup(r.content,'html.parser')

