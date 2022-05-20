import telebot

bot = telebot.TeleBot('5380173958:AAEd9prlHbDWI5tgrgSGFUVv_DK0OKAypzs')
chat_id = 478653567


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(chat_id,"Привет ✌️ ")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(chat_id, "Привет, чем я могу тебе помочь?")
    elif message.text == "Яблоко":
        bot.send_photo(chat_id, open('res/shrek.jpg','rb'))

bot.polling(none_stop=True, interval=0)
