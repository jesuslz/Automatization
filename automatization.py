import sqlite3
import numpy as np
import openpyxl as pxl

'''Create the data base for WASS'''
class CreateDataBase(object):
    def __init__(self, dataBaseName):
        ''' This class just recive the data base name and begin to work,
        Create a connection to Data Base and with this connection we'll create a cursor''' 
        self.connection = sqlite3.connect(dataBaseName)
        self.cursor_db = self.connection.cursor()
    
    '''The next function creates a table within the data base'''
    def createTable(self, tableDataBaseName, tableArgs):
        '''lines 18 to 26 are just an algoritm to create a string
        with the command in sqltie language'''
        com = ''
        aux = 1
        x = tableArgs.items()
        for i, j in x:
            if aux == (len(x)):
                com = com + str(i) + ' ' + str(j)
            else:
                com = com + str(i) + ' ' + str(j) + ', '
            aux += 1

        comando = 'CREATE TABLE IF NOT EXISTS ' + tableDataBaseName + '(' + com + ')'
        self.cursor_db.execute(comando)
    

def main():
    myObject = CreateDataBase('nuevaBasededatos.db')
    diccionario = {'nombre1': 'REAL', 'nombre2': 'TEXT', 'nombre3': 'TEXT', 'nombre4': 'REAL', 'nombre5': 'TEXT'}
    myObject.createTable('Tabla1', diccionario)

if __name__ == '__main__':
    main()