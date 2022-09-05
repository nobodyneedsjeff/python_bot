import telegram
import requests
from telegram.ext import *
from datetime import datetime, timedelta



msg=""
bot_token="***"

bot = telegram.Bot(token=bot_token)
def test(user_input,update ):
    chat_id= str(update.message.chat_id)
    #chat_inf=str(update.telegram.chat(id,type,username))
    input_text = str(user_input).lower()
    local_time= update.message.date+timedelta(hours=5)
    print(local_time.strftime("%d %b %y"))
    print(local_time.strftime("%a %X") + " userID("+str(update.message.from_user.id)+")")
    if str(update.message.chat.type) in ["supergroup","group"]:
        print("From "+str(update.message.chat.type)+" "+ str(update.message.chat.title)+ " groupID("+str(update.message.chat_id)+")")
    else:
        print(str(update.message.chat.type))
    print(str(update.message.from_user.first_name)+ " aka "+str(update.message.from_user.username) +" wrote:")
    print(str(update.message.text))
    #print(str(update.message))
    print("")

    # explaining code below::::
    # this is the lis of words to look for in a text
    image_lookup = ["похож"]  # this is the message sent by user
    # ext in the code below stands for a node in an array, in this case, its "start" and "hi"
    # it can be labeled anything, except for stored variables,

    if any(a in input_text.lower() for a in image_lookup):
        print("nay")

    if input_text in ["/start",'мирка','hello']:
        return "Мирка, хуй соси губой тряси"
    if input_text in ['два плюс два?', '2 плюс 2', '2 + 2']:
        return "хуй знает"
    if input_text in["/mirka_dolbaeb"]:
        return "да"
    if input_text in ['киса']:
        return bot.send_photo(chat_id,photo="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tarvinvets.co.uk%2Fwp-content%2Fuploads%2Fsites%2F13%2F2018%2F04%2FKitten-pack.jpg&f=1&nofb=1")
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
