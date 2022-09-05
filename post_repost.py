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
def test():


    collections.Callable = collections.abc.Callable # ihaveno idea wtf is this but it doesn't work withour it
    req = Request('https://repost.uz',headers={'User-Agent': 'Mozilla/5.0'}) #page link
    htmldata = urlopen(req).read()
    soup = BeautifulSoup(htmldata, 'html.parser') #parces page
    news_post = soup.find('div', class_="big-latest-post" ) #finds div
#
    link=news_post.find("a").get('href') #finds direct link
    print("old old links is : " + str(old_links))
    print("repost.uz"+link) #gets link to the top news
    if old_links[-1] != link:
        old_links.append(link)
        bot.send_message(chat_id=my_chat, text="repost.uz" + link)  # sends message from repost uz
    print("new old links: " + str(old_links))


print(link)
print("")

schedule.every().minutes(15).do(test)

while True:
    schedule.run_pending()