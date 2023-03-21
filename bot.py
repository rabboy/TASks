import telebot
import bd 
Task =''
Year = 0
Month = 0
Day = 0
Hour = 0
Minute = 0


def runBot():
    API_KEY = '6206440201:AAE_wQTzLiIVr6CsC-aWK4AetGxgDl-ewL4'
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
            bot.send_message(message.chat.id, str(bd.printtasks()))
        elif message.text.lower() == 'удалить':
            bot.send_message(message.chat.id, "Какую задачу будем удалять?")
            bot.send_message(message.chat.id, str(bd.printtasks()))
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

    bot.polling()



runBot()