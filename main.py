import bot 
import asyncio
import bd
import timemod as tm
bd.new()

def main():
    task1 = asyncio.create_task(bot.runBot())
    task2 = asyncio.create_task(tm.startdindin(bd.uptask()))
    await task1
    await task2

asyncio.run(main())



