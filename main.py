import os, sys 
import json , re
import telegram 
from pprint import pprint
from telegram.ext import  Updater,CommandHandler ,MessageHandler ,Filters ,StringCommandHandler ,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
updater = Updater(token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
os.system("clear")
print("Bot running")
dispatcher = updater.dispatcher

def conversation(bot, update):

      username = update.message.from_user.username 
      data = update.message.text
      datamsg = 'username :' + username + ' message :'  + data
      with open('data/userchat.txt', 'a') as f:
                  json.dump(datamsg, f, ensure_ascii=False)
      

      if   (data == 'hi' or data == 'hello'or data == 'Hi' or data == 'Hello' ):
            bot.send_message(chat_id=update.message.chat_id, text="Hi @" + username + ", I'm here to assist you. Feel free ask me anything, Boss :")   

      elif   (re.search("how[^install].*kramaos$", data , re.IGNORECASE)):
            bot.send_message(chat_id=update.message.chat_id, text="https://youtu.be/1NZ4XcFevpA")   
            bot.send_message(chat_id=update.message.chat_id, text="https://youtu.be/lWTqxsvEehw")

      elif (re.search("how[^install].*keyboard$", data ,re.IGNORECASE)):
            bot.send_message(chat_id=update.message.chat_id, text=" https://youtu.be/QDWwVHfoByw")
      
      elif (re.search('what can I ask?', data ,re.IGNORECASE)):
            bot.send_message(chat_id=update.message.chat_id, text="Good Question. Now You can ask me about koompi and how to install something on KOSMOS OS .")

      elif (re.search("if you don't answer?", data ,re.IGNORECASE)):
            bot.send_message(chat_id=update.message.chat_id, text="if i do not answer i note your question")
      
      elif (re.search("how to install koompi os", data ,re.IGNORECASE)):
            bot.send_message(chat_id=update.message.chat_id, text="https://youtu.be/1NZ4XcFevpA")   
            bot.send_message(chat_id=update.message.chat_id, text="https://youtu.be/lWTqxsvEehw")


      elif (re.search('how to install KOSMOS v2?', data ,re.IGNORECASE)):
             bot.send_message(chat_id=update.message.chat_id, text="https://youtu.be/1NZ4XcFevpA")   
             bot.send_message(chat_id=update.message.chat_id, text="https://youtu.be/lWTqxsvEehw")

      elif (re.search('thank', data ,re.IGNORECASE)):
            bot.send_message(chat_id=update.message.chat_id, text="thank ;)")

      elif (re.search('about', data ,re.IGNORECASE)):
            bot.send_message(chat_id=update.message.chat_id, text="www.koompi.com")

      elif (re.search('how are you', data ,re.IGNORECASE)):
            bot.send_message(chat_id=update.message.chat_id, text="I'm fine Thank")

      elif (re.search("how", data ,re.IGNORECASE)):
            bot.send_message(chat_id=update.message.chat_id, text="Did you mean, how to install KOSMOS v2?")

      else :
            bot.send_message(chat_id=update.message.chat_id, text="I'm still new to everything KOOMPI, @" + username +".I will inform our team to get back to you soon. Thank you for helping us to improve knowledge in our community with your exploration with KOOMPI and KOSMOS" )   


echo_handler = MessageHandler(Filters.text , conversation)

#end conversation
def option(bot, update):
      
      username = update.message.from_user.username 

      button = [
            [InlineKeyboardButton("How to add new keyboard", callback_data = "@"+username+"\n <a href=\"youtu.be/QDWwVHfoByw\">Channel Youtube</a>")],
            [InlineKeyboardButton("Kroma OS", callback_data="kramaOs"),
                  InlineKeyboardButton("Khmer Keyboard", callback_data="khKey"),
                        InlineKeyboardButton("Chinese  Keyboard", callback_data="cnkey")],
            [InlineKeyboardButton("Bluetooth", callback_data="blue2"),
                  InlineKeyboardButton("Unzip File", callback_data="unZip"),
                        InlineKeyboardButton("Screenshot", callback_data="screenshot")],
            [InlineKeyboardButton("OBS Record", callback_data="oBs"),
                  InlineKeyboardButton("Open office", callback_data="Coming soon..."),
                        InlineKeyboardButton("Buy", callback_data="@"+username+"\nShop : <a href=\"koompi.com/retailers\">Here</a>")]
      ]
      reply_markup = InlineKeyboardMarkup(button)
      bot.sendMessage(chat_id=update.message.chat_id,
                       text="Solution:",         
                       reply_markup=reply_markup)

option_handler = CommandHandler("FAQ", option)



def button(bot, update):
      query = update.callback_query
      print(query.data)
      name = query.from_user.username
      kramaOs = "@" + name + "\n Version English <a href=\"https://youtu.be/lWTqxsvEehw\">Here</a> \n Version Khmer <a href=\"https://youtu.be/1NZ4XcFevpA\">Here</a> "
      khKey = "@" + name + "\n follow is video <a href=\"https://youtu.be/QDWwVHfoByw\">Here</a>"
      cnKey = "@" + name + "\n Open <b>**konsole** </b> then type : \n <code>sudo pacman -S adobe-source-han-sans-cn-fonts</code>"
      blue2 = "@" + name + "\n Open <b>**konsole** </b> then type: <code>sudo pacman -Sy blueman</code> \n then type: <code>sudo systemctl restart bluetooth</code> \n then type: <code>sudo systemctl status bluetooth</code> \n restart your <b>KOOMPI</b>"
      unZip = "@" + name + "\n Open <b>**konsole** </b> then type: <code>pi -i archiver</code>"
      sShot = "@" + name + "\n Open <b>**konsole** </b> then type: <code>pi -i spectacle</code>"
      oBs = "@" + name + "\n Open <b>**konsole** </b> then type: <code>pi -i obs-studio</code>"
      data = query.data
      if (data == "screenshot"):

            bot.sendMessage(chat_id= query.message.chat_id,
                            text= "{}".format(sShot),
                            parse_mode= "html",
                            message_id=query.message.message_id)
      
      elif (data == "kramaOs"):
            bot.sendMessage(chat_id= query.message.chat_id,
                            text= "{}".format(kramaOs),
                            parse_mode= "html",
                            message_id=query.message.message_id)

      elif (data == "khKey"):
            bot.sendMessage(chat_id= query.message.chat_id,
                            text= "{}".format(khKey),
                            parse_mode= "html",
                            message_id=query.message.message_id)

      elif (data == "cnkey"):
            bot.sendMessage(chat_id= query.message.chat_id,
                            text= "{}".format(cnKey),
                            parse_mode= "html",
                            message_id=query.message.message_id)


      elif (data == "blue2"):
            bot.sendMessage(chat_id= query.message.chat_id,
                            text= "{}".format(blue2),
                            parse_mode= "html",
                            message_id=query.message.message_id)

      elif (data == "unZip"):
            bot.sendMessage(chat_id= query.message.chat_id,
                            text= "{}".format(unZip),
                            parse_mode= "html",
                            message_id=query.message.message_id)
      elif (data == "oBs"):
            bot.sendMessage(chat_id= query.message.chat_id,
                            text= "{}".format(oBs),
                            parse_mode= "html",
                            message_id=query.message.message_id)

      else :
           
            bot.sendMessage(chat_id= query.message.chat_id,
                            text=" {}".format(query.data),
                            parse_mode= "html",
                            message_id=query.message.message_id)
      

button_handler = CallbackQueryHandler(button)

#end option 

#about
def about(bot, update):

    bot.sendMessage(chat_id=update.message.chat_id,
                      text="<a href=\"https://www.koompi.com/\">Koompi.com</a>",
                      parse_mode= "html")

    msg = bot.send_photo(chat_id=update.message.chat_id, photo=open("images/chatbot.jpg", "rb"))
    msg2 = bot.send_photo(chat_id=update.message.chat_id, photo=open("images/chatbot2.jpg", "rb"))
    file_id = msg.photo[0].file_id
    file_id1 = msg2.photo[1].file_id
    bot.send_photo(photo=file_id)
    bot.send_photo(photo=file_id1)
    


about_handler = CommandHandler("About", about)

#start
def start(bot, update):
    username = update.message.from_user.username 
    with open('data/userplay.txt', 'a') as f:
                  json.dump(username, f, ensure_ascii=False)
    kb = [[telegram.KeyboardButton('/FAQ'),telegram.KeyboardButton('/About Koompi')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb, resize_keyboard=True)

    bot.send_message(chat_id=update.message.chat_id,
                     text="@"+username,
                     reply_markup=kb_markup)

start_handler = CommandHandler("start", start)

#delete
print("delete sticker")
def delete_sticker(bot, update):
    if update.effective_message.sticker:
        bot.deleteMessage(chat_id = update.message.chat_id, message_id = update.message.message_id)

#send document 
def userchat(bot, update):

      userchat = bot.sendDocument(chat_id=update.message.chat_id, document=open("data/userchat.txt", "rb"))
      file_id = userchat.file_id
      bot.sendDocument(document=file_id)
    
userchat_handler = CommandHandler("userchat", userchat)

#send document Pl
def userplay(bot, update):

      userplay = bot.sendDocument(chat_id=update.message.chat_id, document=open("data/userplay.txt", "rb"))
      file_id = userplay.file_id
      bot.sendDocument(document=file_id)
    
userplay_handler = CommandHandler("userplay", userplay)


 #main   
def main() :
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(button_handler)
    dispatcher.add_handler(option_handler)
    dispatcher.add_handler(about_handler)
    dispatcher.add_handler(userchat_handler)
    dispatcher.add_handler(userplay_handler)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(MessageHandler(Filters.all, delete_sticker))
   
    

if __name__ == '__main__':
    main()
    updater.start_polling()
    updater.idle()
