!pip install adafruit-io
import os
x = os.getenv('x')
y = os.getenv('y')  #Use your own Adafruit Active Key
from Adafruit_IO import Client, Feed
aio = Client(x,y)
new = Feed(name='bot123')     #Creating a new feed
result = aio.create_feed(new)
result
from Adafruit_IO import Data
!pip install python-telegram-bot
from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
def on(bot,update):
  chat_id = update.message.chat_id    
  aio.create_data('bot123',Data(value = 1))
  bot.send_message(chat_id =chat_id,text ="Lights On")

def off(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('bot123',Data(value = 0))
  bot.send_message(chat_id =chat_id,text ="Lights Off")

updater = Updater('1314501154:AAFupk7zdBSYmGlY2cDaSUdYLO4RAfF3TXs')     #Use Telegram Token HTTP API
dp =updater.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
updater.start_polling()
updater.idle()
 
