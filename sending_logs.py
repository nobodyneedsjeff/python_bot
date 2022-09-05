import telegram
import os



my_chat="873556674"
JMD_chat='-1001110252788'
shikandpshik='865546057'
uzbek_news='-1001605744248 '
bot_token="1441076667:AAE7l6g19AQDcASzRUaEzSkYBNAhJqTx-Uw"
borya_chat="250716"

#chat_list=[my_chat,JMD_chat] # list of chats to send message to, can be anything
msg="jmd md" #text to send
file=open("C:\\Users\\NAkanov\PycharmProjects\\tele_bot_new_att\\chats\\873556674_nobodyneedsjeff.txt", "rb")
bot = telegram.Bot(token=bot_token) #bot token
directory=r'C:\Users\NAkanov\PycharmProjects\tele_bot_new_att\chats'
#directory=r'C:\Users\NAkanov\PycharmProjects\tele_bot_new_att\chats'
for files in os.listdir(directory):
    bot.send_document(my_chat, open(os.path.join(directory,files)))
    if files.endswith(".txt"):
        print(os.path.join(directory,files))


print()
print(os.listdir(r'C:\Users\NAkanov\PycharmProjects\tele_bot_new_att\chats'))
