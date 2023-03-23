import bot 
import asyncio
import bd
import timemod as tm
bd.new()

async def main():
    task1 = asyncio.create_task(bot.runBot())
    task2 = asyncio.create_task(tm.startdindin())
    await task1
    await task2

asyncio.run(main())



