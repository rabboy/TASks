import telebot
import asyncio
import bd 
import botAPI as ba
Task =''
Year = 0
Month = 0
Day = 0
Hour = 0
Minute = 0
mci = ''

def checknull(a):
    if a < 10:
        return '0'
    else:
        return ''

def shwtsks(message):
    API_KEY = ba.API_KEY
    bot = telebot.TeleBot(API_KEY)
    bot.send_message(message.chat.id, 'Задачи:')
    for x in bd.printtasks():           
        bot.send_message(message.chat.id, f'"{x[0]}"   {checknull(x[3])}{x[3]}-{checknull(x[2])}{x[2]}-{x[1]} в {checknull(x[4])}{x[4]}:{checknull(x[5])}{x[5]}')

def runBot():
    API_KEY = ba.API_KEY
    bot = telebot.TeleBot(API_KEY)
    @bot.message_handler(commands=['start', 'начать', 'привет'])
    def hello(message):
        bot.send_message(message.chat.id, 'Привет! Напиши "создать" чтобы добавить задачу')

    @bot.message_handler(content_types=['text'])
    def addt(message):
        if message.text.lower() == 'создать':
            bot.send_message(message.chat.id, "Как назовём задачу?")
            bot.register_next_step_handler(message, get_task)
        elif message.text.lower() == 'посмотреть':
            shwtsks(message)
        elif message.text.lower() == 'удалить':
            bot.send_message(message.chat.id, "Какую задачу будем удалять?")
            shwtsks(message)
            bot.register_next_step_handler(message, del_task)
        else :
            bot.send_message(message.chat.id, "Я тебя не понимаю")

    def get_task(message):
        global Task
        Task = message.text
        bot.send_message(message.chat.id, "Напиши год")
        bot.register_next_step_handler(message, get_year)


    def get_year(message):
        global Year
        Year = message.text
        bot.send_message(message.chat.id, "Напиши месяц")
        bot.register_next_step_handler(message, get_month)

    def get_month(message):
        global Month
        Month = message.text
        bot.send_message(message.chat.id, "Напиши день")
        bot.register_next_step_handler(message, get_day)

    def get_day(message):
        global Day
        Day = message.text
        bot.send_message(message.chat.id, "Напиши Час")
        bot.register_next_step_handler(message, get_hour)

    def get_hour(message):
        global Hour
        Hour = message.text
        bot.send_message(message.chat.id, "Напиши минуту")
        bot.register_next_step_handler(message, get_minute)
    
    def get_minute(message):
        global Minute
        Minute = message.text
        bot.send_message(message.chat.id, 'Задача ' + Task + ' должна выполниться ' + str(Day) + ':' + str(Month) + ':' + str(Year) + ' в ' + str(Hour) + ':' + str(Minute) + ' ?')
        bd.add(Task, Year, Month, Day, Hour, Minute)
    
    def del_task(message):
        bd.remove(message.text)
    
    await asyncio.sleep(3)

    bot.polling()

