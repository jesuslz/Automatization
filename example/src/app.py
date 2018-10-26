import os
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def index():
    return render_template('upload.html')

@app.route('/upload', methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    
    for file in request.files.getlist('file'):
        print(file)
        filename = file.filename
        destination = '/'.join([target, filename])
        print('Este es el destino', destination)
        excelfile = '/'.join([APP_ROOT, filename])
        #file.save(destination)
        file.save(excelfile)

        #------------------------Comienzo del codigo Excel------------------------
        import prueba as pr
        name_Workwook = excelfile
        name_Sheet = 'jamu week'
        instanca_Data = pr.PerformancePandas(name_Workwook, name_Sheet)
        '''wos host'''
        encontrados_wos = instanca_Data.busqueda('WOS HOST')
        indice = instanca_Data.obtener_indice()
        # al indice le sumamos 2 para evitar poner el nombre de la tabla y la linea que separa al nombre de los datos
        data_wos = instanca_Data.obtener_data(indice[0][0] + 2)
        data_wos = instanca_Data.text_To_Columns(data_wos)
        '''completed'''
        encontrados_complete = instanca_Data.busqueda('COMPLETECOUNT HOST')
        indice = instanca_Data.obtener_indice()
        data_complete = instanca_Data.obtener_data(indice[0][0] + 2)
        data_complete = instanca_Data.text_To_Columns(data_complete)
        '''failed '''
        encontrados_failed = instanca_Data.busqueda('FAILEDDETAILED')
        indice = instanca_Data.obtener_indice()
        data_failed = instanca_Data.obtener_data(indice[0][0] + 2)
        data_failed = instanca_Data.text_To_Columns(data_failed)
        '''timeout'''
        encontrados_timeout = instanca_Data.busqueda('TIMEOUTDETAILED')
        indice = instanca_Data.obtener_indice()
        data_timeout = instanca_Data.obtener_data(indice[0][0] + 2)
        data_timeout = instanca_Data.text_To_Columns(data_timeout)

        #Convertir a diccionarios para no perder la informacion a la hora de ordenar y alinear
        dictionary_wos = instanca_Data.convert_to_directory(data_wos[:, 1], data_wos[:, 0])
        dictionary_complete = instanca_Data.convert_to_directory(data_complete[:, 1], data_complete[:, 0])
        dictionary_failed = instanca_Data.convert_to_directory(data_failed[:, 1], data_failed[:, 0])
        dictionary_timeout = instanca_Data.convert_to_directory(data_timeout[:, 1], data_timeout[:, 0])
        
        instanca_Data.write_pandas_xlsx_document(instanca_Data.dictionary_to_pyMatrix(dictionary_timeout), 'timeout-JAMU.xlsx')


        instanca_Data.write_pandas_xlsx_document(instanca_Data.dictionary_to_pyMatrix(dictionary_failed), 'failed-JAMU.xlsx')

        '''+*******************ESTA pendiente la linea anterior********************'''


        #Luego que estan los diccionarios hay que alinear los vectores

        data_wos, data_complete = instanca_Data.alignment(
            data_wos[:, 1], data_complete[:, 1])
        data_wos, data_failed = instanca_Data.alignment(data_wos, data_failed[:, 1])
        data_wos, data_timeout = instanca_Data.alignment(data_wos, data_timeout[:, 1])


        #crear cada una de las matrices individuales
        completed_Matrix = instanca_Data.create_Matrix_Excel(
            data_wos, data_complete, dictionary_wos, dictionary_complete)
        failed_Matrix = instanca_Data.create_Matrix_Excel(
            data_wos, data_failed, dictionary_wos, dictionary_failed)
        timeout_Matrix = instanca_Data.create_Matrix_Excel(
            data_wos, data_timeout, dictionary_wos, dictionary_timeout)

        #Crear la matriz completa
        full_Matrix = []
        for i in range(len(data_wos)):
            full_Matrix.append(
                completed_Matrix[i] + failed_Matrix[i][2:] + timeout_Matrix[i][2:])


        #escribir el archivo de excel
        instanca_Data.write_pandas_xlsx_document(full_Matrix, 'Performance-JAMU.xlsx')
    
    return render_template('complete.html')





@app.route('/new')
def say_hello():
    
    return render_template('hello.html')
if __name__ == '__main__':
    app.run(port = 4555, debug = True)



'''
Documenttion:

https://www.youtube.com/watch?v=bxFaa_FNdL4
'''
