import sqlite3
import time
import numpy as np
import matplotlib.pyplot as plt


import openpyxl

#connection = sqlite3.connect('NewBaseData.db')
#cursor_db = connection.cursor()


def create_table():
    
    nombreTable = 'cosas'
    x = {'nombre1': 'REAL', 'nombre2': 'TEXT', 'nombre3': 'TEXT', 'nombre4': 'REAL', 'nombre5': 'TEXT'}
    
    com = ''
    aux = 1
    x = x.items()
    for i, j in x:
        if aux == (len(x)):
            com = com + str(i) + ' ' + str(j)
        else:
            com = com + str(i) + ' ' + str(j) + ', '
        aux += 1
        
    comando = 'CREATE TABLE IF NOT EXISTS ' + nombreTable + '(' + com + ')'
    
    print(comando)
    print(type(comando))
    cursor_db.execute(comando)

#create_table() 

def read_xlsx():
    '''This function will read a xlsx file. The
    xlsm file contains all the information about
    the statistics of the servers'''

    #firs we'll read the file
    file_xlsx = openpyxl.load_workbook('INTE-Performance-WASS-2018.xlsx', data_only= True)
    sheet = file_xlsx['WASSPerformance']
    rng = np.array(list(sheet['B17':'M226']))
    #print(rng.shape[0])
    data = [[sheet.cell(row=j, column=i).value for i in range(2, rng.shape[1] + 2)]for j in range(17,227)]
    data = np.array(data)
    months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
    #print(data[:,3])
    plt.plot(data[:,1])
    plt.plot(data[:,2])
    plt.plot(data[:,4])
    plt.plot(data[:,6])
    plt.plot(data[:,8])
    plt.plot(data[:,10])
    plt.show()
    #Now we will create a numpy data matrix

read_xlsx()
