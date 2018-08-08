import sqlite3
import time
import numpy as np
import matplotlib.pyplot as plt
connection = sqlite3.connect('asap.db')
cursor_db = connection.cursor()

def create_table():
    cursor_db.execute('CREATE TABLE IF NOT EXISTS estadisticasDiarias(day TEXT, total REAL, completeT REAL, completeP REAL, failedT REAL, failedP REAL, in_progT REAL, in_progP REAL, timeoutT REAL, timeoutP REAL, failT REAL, failP REAL)')

def data_entry():
    fecha = time.strftime('%d/%m/%y') #%x imprime la fecha formato ingles
    cursor_db.execute('INSERT INTO estadisticasDiarias(day, total, completeT, completeP, failedT, failedP, in_progT, in_progP, timeoutT, timeoutP, failT, failP) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)', (fecha, 13, 2, 10, 3, 5, 6, 7, 8, 8, 1, 23))
    connection.commit()
    cursor_db.close()
    connection.close()
def read_from_db():
    for i in [13]:
        cursor_db.execute("SELECT * FROM estadisticasDiarias WHERE total < (%f)" %(i))
        data = cursor_db.fetchall()
        print(data)
        data = np.array(data[0][1:])
        print(data[0])
        plt.plot(data)
        plt.show()
    #data = np.array(data)
    #print(data[:,0])
#create_table()
#data_entry()
read_from_db()

'''
def create_table():
    connection = sqlite3.connect('pythonsqlite.db')
    cursor_db = connection.cursor()
    cursor_db.execute('CREATE TABLE IF NOT EXISTS projects(name TEXT, begin_date TEXT,end_date TEXT)')

create_table()
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def main():
    database = "pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1,
                  1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements',
                  1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)


if __name__ == '__main__':
    main()
'''