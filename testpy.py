import telegram
import requests
from telegram.ext import *
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import collections






req = Request('https://repost.uz/category/uzbekistan', headers={'User-Agent': 'Mozilla/5.0'})
htmldata = urlopen(req).read()

collections.Callable = collections.abc.Callable  # ihaveno idea wtf is this but it doesn't work withour it
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')
#item=  images.find_all('src')

for item in images:
    print(item['src'])

