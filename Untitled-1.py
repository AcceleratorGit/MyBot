import telebot
bot = telebot.TeleBot('5920353752:AAGvOaEVPaEem-W95dWv77bu7OjxeoNhF8U')
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет', parse_mode='html')

bot.polling(none_stop=True)