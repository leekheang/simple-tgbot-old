import telegram 
from telegram.ext import Updater,CommandHandler,Filters,MessageHandler
import os, sys

updater = Updater(token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
os.system("clear")
print("Bot running")
dispatcher = updater.dispatcher

#about
def about(bot, update):

    bot.sendMessage(chat_id=update.message.chat_id,
                      text=" Please talk to our Assistant via @KOOMPIbot")

about_handler = CommandHandler("About", about)

#start
def start(bot, update):
    username = update.message.from_user.username 
    bot.send_message(chat_id=update.message.chat_id,
                     text="@"+username + " Please talk to our Assistant via @KOOMPIbot")

start_handler = CommandHandler("start", start)

#delete
print("delete sticker")
def delete_sticker(bot, update):
    if update.effective_message.sticker:
        bot.deleteMessage(chat_id = update.message.chat_id, message_id = update.message.message_id)

 #main   
def main() :
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(about_handler)
    dispatcher.add_handler(MessageHandler(Filters.all, delete_sticker)) 
if __name__ == '__main__':
    main()
    updater.start_polling()
    updater.idle()
