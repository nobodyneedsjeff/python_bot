import telegram
import collections
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


import schedule



my_chat="873556674"
uzbek_news='********* '
bot_token="**********"
bot = telegram.Bot(token=bot_token) #bot token
JMD_chat='-1001110252788'
old_links = ['']
link=''
def post_repost():


    collections.Callable = collections.abc.Callable # ihaveno idea wtf is this but it doesn't work withour it
    req = Request('https://repost.uz',headers={'User-Agent': 'Mozilla/5.0'}) #page link
    htmldata = urlopen(req).read()
    soup = BeautifulSoup(htmldata, 'html.parser') #parces page
    news_post = soup.find('div', class_="list-latest-posts" ) #finds div
#
    link_to_small=news_post.find_all("a") #finds direct link
    link=link_to_small[0].get("href")
    print("old old links is : " + str(old_links))
    print("repost.uz"+str(link)) #gets link to the top news
    if old_links[-1] != link:
        old_links.append(link)
        #bot.send_message(chat_id=my_chat, text="repost.uz" + link)  # sends message from repost uz
    print("new old links: " + str(old_links))

test()
print("")

schedule.every(30).minutes.do(post_repost)

while True:
    schedule.run_pending()
