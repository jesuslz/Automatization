import Performance as Pce
import pandas as pd
import numpy as np

class PerformancePandas(Pce.Performance):
    def __init__(self, nameWorkbook, nameSheet):
        try:
            self.file_pandas = pd.read_excel(nameWorkbook, sheet_name=nameSheet)
            self.data_pandas = np.array(self.file_pandas)
            
        except:
            print('Possible list of error: \n -> The workbook is not in this directory \n -> The workbook name is incorrect \n -> The Name Sheet is not correct or not exists')
        
    def similitud(self, search_chain, find_chain):
        self.N_len = len(find_chain)
        self.n_len = len(search_chain)

        return self.n_len / self.N_len
    
    def convert_to_directory(self, list_1, list_2):
        '''Esta funcion convierte dos listas con las
        mismas dimensiones a un diccionario
        la lista 1 corresponde a las keys
        la lista 2 corresponde a los valores'''

        list_1 = [str(i) for i in list_1]
        list_2 = [float(i) for i in list_2]

        self.dictionary = dict(zip(list_1, list_2))

        return self.dictionary

        '''
        https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary-in-python
        
        '''

    def dictionary_to_pyMatrix(self, dictionary):
        self.pyMatrix = list(dictionary.items())
        self.pyMatrix.sort(key=lambda x: -x[1])

        '''
        key = lambda x : x[0] de menor a mayor con los keys
        key = lambda x : -x[0] de mayor a menor con los keys 
        key = lambda x : -x[1] de mayor a menor con los values
        key = lambda x : x[1] de menor a mayor con los values

        '''

        return self.pyMatrix

    def busqueda(self, palabra_de_busqueda):
        self.encontrados = []
        for self.i in self.data_pandas[:,0]:
            self.i = str(self.i)
            if palabra_de_busqueda in self.i:
                self.encontrados.append(list((self.i, self.similitud(palabra_de_busqueda, self.i))))
        
        '''Hay que regresar la lista ordenada
        primero necesitamos saber cual es el que tiene mas
        coincidencia, para ello haremos diccionarios y luego
        haremos una lista ordenando las probabilidades de mayor a 
        menor para luego quedarnos con el primer'''
        self.aux_numpy_list = np.array(self.encontrados)
        #print(self.aux_numpy_list[:,1])
        self.aux_dictionary = self.convert_to_directory(self.aux_numpy_list[:,0], self.aux_numpy_list[:,1])
        self.encontrados = self.dictionary_to_pyMatrix(self.aux_dictionary)

        return self.encontrados

    def obtener_indice(self):

        return np.where(self.data_pandas == self.encontrados[0][0])#siempre es la posicion 0,0 porque la lista ya esta ordenada
    
    def obtener_data(self, index):
        self.tabla = []
        for i in self.data_pandas[index:, 0]:
            i = str(i)
            if 'rows selected' in i:
                break
            else:
                self.tabla.append(i)

        return self.tabla

    def text_To_Columns(self, Matrix):
        try:
            '''Matriz de Numpy con datos y con columnas separadas'''
            self.numpy_matrix = np.array([Matrix[i].split()
                                          for i in range(len(Matrix))])
        except:
            print('En alguna de las filas de la matriz no hay datos, verifiue las dimensiones de la matriz que paso')

        '''NOTA ------>>>>> No importa que en el excel no se haya 
           hecho la funcion text to columns, 
           puede mandarsele una matriz que contenga a vector con la 
           informacion ya que no toma en cuenta espacios en blanco'''
        return self.numpy_matrix
    
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

        return self.sortMatrix


    def write_pandas_xlsx_document(self, dataMatrix, fileName):
        
        self.excel_file = pd.DataFrame(dataMatrix)
        self.excel_file.to_excel(fileName)
    
    '''def write_pandas_xlsx_document_dictionary(self, dictionary, fileName):
        matrix = []
        for i, j in dictionary.items():
            matrix.append(list((i, j)))

        self.excel_d_file = pd.DataFrame(matrix)
        self.excel_d_file.to_excel(fileName) '''
