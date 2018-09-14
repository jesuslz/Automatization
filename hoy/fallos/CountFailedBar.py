'''Esta clase contiene una serie de pasos para
hacer una clasificacion entre los datos fallados
de la plataforma de BAR_COMG en WASS'''
import pandas as pd 
import numpy as np 
class CountFailedBar():
    def __init__(self, NameFile, nameSheet, skiprows_0, rango_nrows):
        self.data = pd.read_excel(NameFile, sheet_name = nameSheet, usecols='A', skiprows=(skiprows_0), nrows=rango_nrows)
        self.data = np.array(self.data)

    def text_Columns(self): #Esta funcion solo divide y crea celdas por palabra
        self.matrix_data = np.array([self.data[i][0].split() for i in range(len(self.data))])
        return self.matrix_data
    
    def clean_all_data(self, matrix):
        '''Esta funcion limpia los datos y solo deja las 
        filas que contienen informacion con la 
        cantidad de errores'''
        self.matr = []
        for i in range(len(matrix)):
            try:
                int(matrix[i][0])
                self.matr.append(matrix[i][:])
            except:
                pass
        self.matr = np.array(self.matr)
        return self.matr
    
    def clasificar_null_account(self, matrix, null_list, account_list):
        '''esta funcion recibe la matriz de datos y dos listas vacias para
        clasificar los datos, en un lista se guardaran todos los datos con
        cuenta vacia, y en la otra todos los datos que tienen una cuenta
        asignada'''

        for i in range(len(matrix)):
            if 'NULL' in matrix[i][:]:
                null_list.append(matrix[i])
                matrix[i] = None
            else:
                account_list.append(matrix[i])
                matrix[i] = None
        
        return null_list, account_list
    
    def clasificar_520_513_another(self, null_list, null_513, null_520, null_another):
        '''Esta funcion clasifica entre los que son nulos con sus correspondientes 
        codigos de error ####pendiente generalizar esta funcion para que reciba una
        lista de todos los posibles errores### en esta situacion solo resuelve para
        dos errores'''
        for i in range(len(null_list)):
            if '513' in null_list[i]:
                null_513.append(null_list[i])
                null_list[i] = None
            elif '520' in null_list[i]:
                null_520.append(null_list[i])
                null_list[i] = None
            else:
                null_another.append(null_list[i])
                null_list[i] = None
        
        return null_513, null_520, null_another

