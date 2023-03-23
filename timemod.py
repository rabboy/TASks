import datetime as dt
import bd
import telebot
import asyncio
import botAPI as ba

async def startdindin():
    while True:
        task = bd.uptask()
        if task != None:
            cursordate = dt.datetime(int(task[1]), int(task[2]), int(task[3]), int(task[4]), int(task[5]))
            nowdate = dt.datetime.now()
            while cursordate > nowdate:
                nowdate = dt.datetime.now()
                await asyncio.sleep(3)
            API_KEY = ba.API_KEY
            bot = telebot.TeleBot(API_KEY)
            bot.send_message(task[6], f'Динь-динь! {task[0]} ждёт!')
            bd.remove(task[0], task[6])
        else:
            await asyncio.sleep(3)


    
    
