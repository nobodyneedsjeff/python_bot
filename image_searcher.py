#works with small pics but here we go :
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import random
import collections



search=['dogs','cats','dragons','gargoyles','rast','mice','kitten']
#random_search=
collections.Callable = collections.abc.Callable
#req = Request('https://www.google.com/search?q='+search[random.randrange(0,len(search))]+'&client=firefox-b-d&sxsrf=ALiCzsb5EhllqQkXemDmmg6IaL03yjLOvw:1660584295330&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiPu6vIrsn5AhWHk4sKHdw4BpAQ_AUoAXoECAEQBA&biw=1920&bih=965&dpr=1', headers={'User-Agent': 'Mozilla/5.0'})
req = Request('https://repost.uz/category/uzbekistan', headers={'User-Agent': 'Mozilla/5.0'})
htmldata = urlopen(req).read()

 #= urlopen('')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')
#item=  images.find_all('src')
limit=len(images)
image_randomizer=images[random.randrange(1,limit)]['src'];
for item in images:
    print(item['src'])
print("")
print(image_randomizer)


print(len(images))
    #print(images.length)