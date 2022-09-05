import telegram
from telegram.ext import *
from datetime import datetime, timedelta
import os



bot_token="*******"

my_chat="873556674"
bot = telegram.Bot(token=bot_token)

def logging_chat(update):
    local_time = update.message.date + timedelta(hours=5)
    local_date = local_time.strftime("%d %b %y")  # date
    local_time = local_time.strftime("%a %X")  # time
    user_id = update.message.from_user.id  # user id
    chat_type = update.message.chat.type  # chat type
    name_of_chat = update.message.chat.title  # chat name
    chat_id = str(update.message.chat_id)  # chat id
    first_name = update.message.from_user.first_name  # first name, user name
    nickname = update.message.from_user.username  # user nickname
    message_itself = update.message.text  # message
    note = [local_date, '\n', local_time, '\n', chat_type, ' ', name_of_chat," ", chat_id, '\n',user_id,' ',first_name, ' aka ', nickname, '\n',"- ", message_itself, '\n']
    if str(update.message.chat.type) in ["supergroup","group"]:
        log_name= chat_id+"_"+name_of_chat
    else:
        log_name=str(user_id)+"_"+str(nickname)
        with open("\\tele_bot_new_att\chats\\"+str(log_name)+".txt",'a') as f: #open file that has name of a user
            for item in note:
                f.write(str(item))
            f.write('\n')
    directory=r'C:\Users\NAkanov\PycharmProjects\tele_bot_new_att\chats'#location of files
    if user_id == my_chat: #applying admin priveleges
        if  message_itself.lower() in "эй бот,": #calling bot
            if message_itself.lower() in "лог": #if i ask for logs
                for files in os.listdir(directory): #look up all the files in logs
                    if files.endswith(".txt"): #check if file has txt ending
                        bot.send_document(my_chat, open(os.path.join(directory,files))) #send files to me
def handle_messages(update,context):
    logging_chat(update)


updater = Updater(bot_token)
d = updater.dispatcher
d.add_handler(MessageHandler(Filters.text, handle_messages))
updater.start_polling()
updater.idle()
