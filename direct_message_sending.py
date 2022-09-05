import telegram
import requests
from telegram.ext import *



my_chat="873556674"
JMD_chat='-1001110252788'
shikandpshik='865546057'
uzbek_news='-1001605744248 '
bot_token="****"
borya_chat="250716"

chat_list=[my_chat,JMD_chat] # list of chats to send message to, can be anything
msg="jmd md" #text to send
bot = telegram.Bot(token=bot_token) #bot token
def test():

    for item in chat_list: #to send message massively to all chats in chat_list
        bot.send_message(chat_id=item, text=msg )

test()
    #   -1001110252788 JMD chat
    #   865546057 shik and pshik
    #   873556674  me
    #   -1001605744248  uzbek news channel
