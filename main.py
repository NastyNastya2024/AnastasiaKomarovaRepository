import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot(token='7026153756:AAHCWgO6LrfA8x-uaIpOq1t1EhQuetocvmQ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат-бот, который будет напоминать тебе пить водичку')
    reminder_thread = threading.Thread(target=send_reminder, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    list = ['Гидратация: Вода помогает поддерживать оптимальный уровень гидратации организма, участвуя в процессах терморегуляции и увлажнения тканей.',
            'Пищеварение: Вода необходима для правильного пищеварения, поскольку помогает в растворении пищи, усвоении питательных веществ и выведении продуктов обмена веществ',
            'Мозговая деятельность: Достаточное употребление воды способствует улучшению концентрации, памяти и когнитивных функций мозга.',
            'Очищение организма: Вода играет важную роль в выведении токсинов и шлаков из организма через мочевыводящие пути.',
            'Кожа: Правильное употребление воды способствует улучшению состояния кожи, делая ее более упругой, сияющей и увлажненной.']
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о воде. {random_fact}')

def send_reminder(chat_id):
    first_rem = "8:00"
    second_rem = "10:00"
    third_rem = "12:00"
    fourth_rem = "14:00"
    fifth_rem = "16:00"
    sixth_rem = "18:00"
    seventh_rem = "21:57"

    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == third_rem or now == fourth_rem or now == fifth_rem or now == sixth_rem or now == seventh_rem:
            bot.send_message(chat_id, text="Пора пополнить запасы своего тела стаканом воды")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)