import sqlite3 as sl
# import timemod as tm

def new():
    tskdb = sl.connect('tasksdatabase.db')
    cur = tskdb.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tasks (
        task TEXT,
        year INT,
        month INT,
        day INT,
        hour INT,
        minute INT,
        user_id INT
    )""")
    tskdb.commit()



def add(TSK, Y, MO, D, H, MI, ID):
    tskdb = sl.connect('tasksdatabase.db')
    cur = tskdb.cursor()
    cur.execute("SELECT task FROM tasks")
    cur.execute(f"INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?)", (TSK, Y, MO, D, H, MI, ID))
    tskdb.commit()


def printtasks(ID):
    tskdb = sl.connect('tasksdatabase.db')
    cur = tskdb.cursor()
    alltasks = []
    for value in cur.execute(f"SELECT * FROM tasks WHERE user_id ='{ID}' ORDER BY year, month, day, hour, minute"):
        alltasks.append(value)
    return alltasks

def remove(TSK, ID):
    tskdb = sl.connect('tasksdatabase.db')
    cur = tskdb.cursor()
    cur.execute(f"DELETE FROM tasks WHERE task = '{str(TSK)}' AND user_id ='{ID}'")
    tskdb.commit()

def uptask():
    tskdb = sl.connect('tasksdatabase.db')
    cur = tskdb.cursor()
    cur.execute(f"SELECT * FROM tasks ORDER BY year, month, day, hour, minute")
    return(cur.fetchone())







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