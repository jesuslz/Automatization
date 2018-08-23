import openpyxl
import numpy as np


class Performance(object):
    def __init__(self, NameFile, NameSheet):
        try:
            self.file_xlsx = openpyxl.load_workbook(NameFile, data_only=True)
            self.sheet = self.file_xlsx[NameSheet]
        except:
            print('Possible list of error: \n -> The workbook is not in this directory \n -> The workbook name is incorrect \n -> The Name Sheet is not correct or not exists')
        
    
    def text_To_Columns(self, a_limitMatrix, b_limitMatrix):
        try:
            '''Lectura directa del workbook'''
            self.excel_matrix = np.array(list(self.sheet[a_limitMatrix: b_limitMatrix]))

            '''Conversion del objeto leido en el paso anterior a una matriz
            con elementos del tipo del objeto excel aun'''
            self.python_matrix = [[self.excel_matrix[i][j].value for j in range(
                                   self.excel_matrix.shape[1])]for i in range(self.excel_matrix.shape[0])]

            '''Matriz de Numpy con datos y con columnas separadas'''
            self.numpy_matrix = np.array([self.python_matrix[i][0].split()
                                    for i in range(len(self.python_matrix))])
        except:
            print('En alguna de las filas de la matriz no hay datos, verifiue las dimensiones de la matriz que paso')
       
        
        
        '''NOTA ------>>>>> No importa que en el excel no se haya 
           hecho la funcion text to columns, 
           puede mandarsele una matriz que contenga a vector con la 
           informacion ya que no toma en cuenta espacios en blanco'''
        return self.numpy_matrix

    def convert_to_directory(self, list_1, list_2):
        '''Esta funcion convierte dos listas con las
        mismas dimensiones a un diccionario
        la lista 1 corresponde a las keys
        la lista 2 corresponde a los valores'''

        list_1 = [str(i) for i in list_1]
        list_2 = [int(i) for i in list_2]

        self.dictionary = dict(zip(list_1, list_2))

        return self.dictionary

        '''
        https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary-in-python
        
        '''


    def alignment(self, a, b):
        '''El primer parametro de esta funcion siempre debe ser
        el vector base'''
        self.a_list = list(a)
        self.b_list = list(b)
        self.a_list.sort()
        self.b_list.sort()
        #hacerlos del mismo tamaño
        for i in range(len(self.a_list)-len(self.b_list)):
            self.b_list.append(None)

        for i in range(len(self.a_list)):
            if not self.a_list[i] == self.b_list[i]:
                self.b_list.insert(i, None)
                self.b_list.pop(-1)

        return self.a_list, self.b_list

    def create_Matrix_Excel(self, list_Base, list_Sec, dic_Base, dic_Sec):
        
        self.sortMatrix = []

        for i in range(len(list_Base)):
            try:
                self.sortMatrix.append(list((int(dic_Base[list_Base[i]]),
                                list_Base[i],
                                int(dic_Sec[list_Base[i]]),
                                list_Sec[i])))
            except:
                self.sortMatrix.append(list((int(dic_Base[list_Base[i]]),
                                list_Base[i], None, None)))
        
        return  self.sortMatrix


    def write_xlsx_Document(self, matrix_data, file_name):

        from openpyxl import Workbook
        self.book = Workbook()
        self.sheet = self.book.active

        for row in matrix_data:
            self.sheet.append(row)
            #print(row)

        self.book.save(file_name)

    def dictionary_to_pyMatrix(self, dictionary):
        self.pyMatrix = list(dictionary.items())
        self.pyMatrix.sort(key = lambda x: -x[1])
        
        '''
        key = lambda x : x[0] de menor a mayor con los keys
        key = lambda x : -x[0] de mayor a menor con los keys 
        key = lambda x : -x[1] de mayor a menor con los values
        key = lambda x : x[1] de menor a mayor con los values

        '''

        return self.pyMatrix

    
