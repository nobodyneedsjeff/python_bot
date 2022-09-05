import telegram

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import collections
import schedule



my_chat="873556674"
uzbek_news='-1001605744248 '
bot_token="1441076667:AAE7l6g19AQDcASzRUaEzSkYBNAhJqTx-Uw"
bot = telegram.Bot(token=bot_token) #bot token
JMD_chat='-1001110252788'
old_links = ['']
link=''
def post_gazeta():


    collections.Callable = collections.abc.Callable # ihaveno idea wtf is this but it doesn't work withour it
    req = Request('https://gazeta.uz/ru',headers={'User-Agent': 'Mozilla/5.0'}) #page link
    htmldata = urlopen(req).read()
    soup = BeautifulSoup(htmldata, 'html.parser') #parces page
    news_post = soup.find('div', class_="newsblock-2" ) #finds div
#
    link_to_small=news_post.find_all("a") #finds direct link
    link=link_to_small[0].get("href")
    print("old old links is : " + str(old_links))
    print("gazeta.uz/ru"+str(link)) #gets link to the top news
    if old_links[-1] != link:
        old_links.append(link)
        bot.send_message(chat_id=uzbek_news, text="gazeta.uz" )  # sends message from repost uz
    print("new old links: " + str(old_links))

test()
print("")

schedule.every(30).minutes.do(post_gazeta)

while True:
    schedule.run_pending()