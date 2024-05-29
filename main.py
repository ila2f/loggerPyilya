import telebot
import time
import schedule

API_TOKEN = '7231901447:AAGErhmZHFGdXUL_XOGW73PqxIjj2iKbZeY'
bot = telebot.TeleBot(API_TOKEN)
id_al = 1518208491


@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    if id_al == chat_id:
        bot.send_message(id_al, "Привет ✌️ log python pro")
    else:
        bot.send_message(message.chat.id, "Привет, бот тебе недоступен")

        @bot.message_handler(commands=['log'])  #
        def send_message_user(message):
            if message.from_user.id == id_al:  # id пользователя
                bot.send_document(message.chat.id, open('./logs/log.txt'))
            else:
                bot.send_message(message.chat.id, 'Бот тебе недоступен')

        def send_file():
            bot.send_document(id_al, open('./logs/log.txt'))
            schedule.every().day.at("8:55").do(send_file())

bot.infinity_polling()


while True:
    schedule.run_pending()
    time.sleep(1)
