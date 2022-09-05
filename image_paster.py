import telegram
import requests
from telegram.ext import *
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import random
import collections





bot_token="1441076667:AAE7l6g19AQDcASzRUaEzSkYBNAhJqTx-Uw"

bot = telegram.Bot(token=bot_token)
def test(user_input,update ):
    chat_id= str(update.message.chat_id) #return chat id

    input_text = str(user_input).lower() #text inserted by user
    local_time= update.message.date+timedelta(hours=5)  #make time tashkent time
    print(local_time.strftime("%d %b %y"))  #print date
    print(local_time.strftime("%a %X") + " userID("+str(update.message.from_user.id)+")")   #print user id and atc
    if str(update.message.chat.type) in ["supergroup","group"]:     #print group or not a grou[
        print("From "+str(update.message.chat.type)+" "+ str(update.message.chat.title)+ " groupID("+str(update.message.chat_id)+")")
    else:
        print(str(update.message.chat.type))
    print(str(update.message.from_user.first_name)+ " aka "+str(update.message.from_user.username) +" wrote:") #name of the user and Also Known As
    print(str(update.message.text)) #print message itself
    #print(str(update.message))
    print("")

    # explaining code below::::
    # this is the lis of words to look for in a text
    image_lookup = ["похож"]  # this is the message sent by user
    # ext in the code below stands for a node in an array, in this case, its "start" and "hi"
    # it can be labeled anything, except for stored variables,
    specify_me=["я"]
    if any(a in input_text.lower() for a in image_lookup):
        if str(update.message.from_user.id) in '873556674':
            if any(a in input_text.lower() for a in specify_me):
                search = ['superman','batman','the+flash','bruce+wayne','clark+kent']
            else:
                search = ['dogs', 'cats', 'dragons', 'gargoyles', 'rast', 'mice', 'kitten']
        else:
            search = ['dogs', 'cats', 'dragons', 'gargoyles', 'rast', 'mice', 'kitten']
        collections.Callable = collections.abc.Callable
        req = Request('https://www.google.com/search?q=' + search[random.randrange(0,len(search))] + '&client=firefox-b-d&sxsrf=ALiCzsb5EhllqQkXemDmmg6IaL03yjLOvw:1660584295330&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiPu6vIrsn5AhWHk4sKHdw4BpAQ_AUoAXoECAEQBA&biw=1920&bih=965&dpr=1',headers={'User-Agent': 'Mozilla/5.0'})
        htmldata = urlopen(req).read()
        soup = BeautifulSoup(htmldata, 'html.parser')
        images = soup.find_all('img')
        limit = len(images)
        image_randomizer=images[random.randrange(1,limit)]['src'];
        return bot.send_photo(chat_id,photo=image_randomizer)

#   -1001110252788 JMD chat
#   865546057 shikandpshik
#   873556674  me
#   -1001605744248  uzbek news channel
   # bot.send_message(chat_id="873556674", text=msg, parse_mode=telegram.ParseMode.HTML)


def handle_messages(update,context):
    text = str(update.message.text)
    response = test(text,update)
    try:
        update.message.reply_text(response)
        print("bot replied: " + response)
        print("")
    except:
        return None

updater = Updater(bot_token)
d = updater.dispatcher
d.add_handler(MessageHandler(Filters.text, handle_messages))
updater.start_polling()
updater.idle()