import sqlite3 as sl


# tskdb = sl.connect('tasksdatabase.db')


# cur = tskdb.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
#     task TEXT,
#     year INT,
#     month INT,
#     day INT,
#     hour INT,
#     minute INT
# )""")
# tskdb.commit()



def add(TSK, Y, MO, D, H, MI):
    tskdb = sl.connect('tasksdatabase.db')
    cur = tskdb.cursor()
    cur.execute("SELECT task FROM tasks")
    cur.execute(f"INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?)", (TSK, Y, MO, D, H, MI))
    print('Задача добавлена!')
    tskdb.commit()

def printtasks():
    tskdb = sl.connect('tasksdatabase.db')
    cur = tskdb.cursor()
    alltasks = []
    for value in cur.execute("SELECT * FROM tasks"):
        alltasks.append(value)
    return alltasks

def remove(TSK):
    tskdb = sl.connect('tasksdatabase.db')
    cur = tskdb.cursor()
    cur.execute(f"DELETE FROM tasks WHERE task = '{str(TSK)}'")
    tskdb.commit()





# if cur.fetchone() is None:
#     cur.execute(f"INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?)", (tsk, h, mo, d, h, mi))
#     tskdb.commit()
# else:
#     print('Такая запись уже имеется!')


# tsk = input('task: ')
# y = input('year: ')
# mo = input('month: ')
# d = input('day: ')
# h = input('hour: ')
# mi = input('minute: ')