import datetime as dt
import asyncio


def startdindin(task):
    for i in range(1, 6):
        task[i] = int(task[i])
    cursordate = dt.datetime(task[1], task[2], task[3], task[4], task[5])
    nowdate = dt.datetime.now()
    while cursordate > nowdate:
        nowdate = dt.datetime.now()
        await asyncio.sleep(3)
    

    
    
