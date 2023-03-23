import telebot
import asyncio
import bd 
from telebot import types
import botAPI as ba
Task =''
Year = 0
Month = 0
Day = 0
Hour = 0
Minute = 0
bd.new()




async def runBot():
    await asyncio.sleep(3)
    API_KEY = ba.API_KEY
    bot = telebot.TeleBot(API_KEY)
    @bot.message_handler(commands=['start', 'начать', 'привет'])
    def hello(message):
        # markupstart = types.InlineKeyboardMarkup()
        # btnmenu = types.InlineKeyboardButton("Меню", callback_data='menu')
        # markupstart.add(btnmenu) 
        # bot.send_message(message.chat.id, 'Привет! Я - Бот-ежедневник, могу хранить все твои дедлайны. ', reply_markup=markupstart)
        bot.send_message(message.chat.id, 'Привет! Я - Бот-ежедневник, могу хранить все твои дедлайны. ')
        mainmenu(message)


    @bot.message_handler(content_types=['text'])
    def menu(message):
        if message.text.lower() == 'добавить':
            bot.send_message(message.chat.id, "Как назовём задачу?")
            bot.register_next_step_handler(message, get_task)
        elif message.text.lower() == 'посмотреть':
            bot.send_message(message.chat.id, 'Задачи:')
            shwtsks(message)
            mainmenu(message)
        elif message.text.lower() == 'удалить':
            bot.send_message(message.chat.id, "Какую задачу будем удалять?")
            shwtsks(message)
            bot.register_next_step_handler(message, del_task)
        else :
            bot.send_message(message.chat.id, "Я тебя не понимаю")
            mainmenu(message)
    
    def mainmenu(message):
        # markupmenu = types.InlineKeyboardMarkup(row_width=2)
        # btnadd = types.InlineKeyboardButton("Добавить задачу", callback_data='addtask')
        # btndel = types.InlineKeyboardButton("Удалить задачу", callback_data='deltask')
        # btnshw = types.InlineKeyboardButton("Посмотреть задачи", callback_data='showtasks')
        # markupmenu.add(btnadd, btndel, btnshw)
        # bot.send_message(message.chat.id, "Меню", reply_markup=markupmenu)
        # bot.send_message(message.chat.id, "Меню: ")
        bot.send_message(message.chat.id, "Меню:")

    def get_task(message):
        global Task
        Task = message.text
        bot.send_message(message.chat.id, "Напиши год")
        bot.register_next_step_handler(message, get_year)

    def get_year(message):
        if tryint(message.text):
            bot.send_message(message.chat.id, "Введи положительное число!!!")
            bot.register_next_step_handler(message, get_year)
        else:
            global Year
            Year = message.text
            bot.send_message(message.chat.id, "Напиши месяц")
            bot.register_next_step_handler(message, get_month)

    def get_month(message):
        if tryint(message.text):
            bot.send_message(message.chat.id, "Введи положительное число!!!")
            bot.register_next_step_handler(message, get_month)
        else:
            global Month
            Month = message.text
            bot.send_message(message.chat.id, "Напиши день")
            bot.register_next_step_handler(message, get_day)

    def get_day(message):
        if tryint(message.text):
            bot.send_message(message.chat.id, "Введи положительное число!!!")
            bot.register_next_step_handler(message, get_day)
        else:
            global Day
            Day = message.text
            bot.send_message(message.chat.id, "Напиши Час")
            bot.register_next_step_handler(message, get_hour)

    def get_hour(message):
        if tryint(message.text):
            bot.send_message(message.chat.id, "Введи положительное число!!!")
            bot.register_next_step_handler(message, get_hour)
        else:
            global Hour
            Hour = message.text
            bot.send_message(message.chat.id, "Напиши минуту")
            bot.register_next_step_handler(message, get_minute)
    
    def get_minute(message):
        if tryint(message.text):
            bot.send_message(message.chat.id, "Введи положительное число!!!")
            bot.register_next_step_handler(message, get_minute)
        else:
            global Minute
            Minute = message.text
            bot.send_message(message.chat.id, 'Задача ' + Task + ' должна выполниться ' + str(Day) + ':' + str(Month) + ':' + str(Year) + ' в ' + str(Hour) + ':' + str(Minute) + ' ?')
            bot.register_next_step_handler(message, regtask)
    
    def regtask(message):
        if message.text.lower() == 'да':
            bd.add(Task, Year, Month, Day, Hour, Minute, message.chat.id)
            bot.send_message(message.chat.id, "Задача добавлена!")
        else:
            bot.send_message(message.chat.id, "Задача не добавлена")
        mainmenu(message)
    
    def del_task(message):
        bd.remove(message.text, message.chat.id)
        bot.send_message(message.chat.id, "Задача " + message.text + " удалена!") 
        mainmenu(message)
    
    def shwtsks(message):
        API_KEY = ba.API_KEY
        bot = telebot.TeleBot(API_KEY)
        for x in bd.printtasks(message.chat.id):           
            bot.send_message(message.chat.id, f'"{x[0]}"   {checknull(x[3])}{x[3]}-{checknull(x[2])}{x[2]}-{x[1]} в {checknull(x[4])}{x[4]}:{checknull(x[5])}{x[5]}')

    def tryint(num):
        try:
            num = int(num)
            if num < 0:
                raise ValueError()
        except:
            return True
        else:
            return False

    def checknull(a):
        if a < 10:
            return '0'
        else:
            return ''
  
    # @bot.callback_query_handler(func=lambda call:True)
    # def menubuttons(call):
    #     if call.message:
    #         if call.data == 'menu':
    #             mainmenu(call.message)
    #         elif call.data == 'addtask':
    #             bot.send_message(call.message.chat.id, "Как назовём задачу?")
    #             bot.register_next_step_handler(message, get_task)
    #         elif call.data == 'deltask':
    #             bot.send_message(call.message.chat.id, "Какую задачу будем удалять?")
    #             shwtsks(call.message)
    #             bot.register_next_step_handler(message, del_task)
    #         elif call.data == 'showtasks':
    #             bot.send_message(call.message.chat.id, "Задачи:")
    #             shwtsks(call.message)
    #             bot.register_next_step_handler(message, returntomenu)





    

# runBot()
























async def startdindin():
    for i in range(1, 6):
        task[i] = int(task[i])
    cursordate = dt.datetime(task[1], task[2], task[3], task[4], task[5])
    nowdate = dt.datetime.now()
    while cursordate > nowdate:
        nowdate = dt.datetime.now()
        await asyncio.sleep(3)
    API_KEY = ba.API_KEY
    bot = telebot.TeleBot(API_KEY)
    bot.send_message(task[6], f'Динь-динь! {task[0]} ждёт!')


async def main():
    task1 = asyncio.create_task(bot.runBot())
    task2 = asyncio.create_task(tm.startdindin())
    await task1
    await task2


# asyncio.run(main())
