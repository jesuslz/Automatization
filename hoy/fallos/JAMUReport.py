import prueba as pr 
name_Workwook = 'FLOW Operation and support report ASAP 7.0.2 JAMU66%2c WASS133 2018-09-03.xlsx'
name_Sheet = 'WASS WEEK'
'''
object1 = pr.PerformancePandas(name_Workwook, name_Sheet)
encontrados = object1.busqueda('WASS BAR_COMG')#regresa estadisticas de las coincidencias encontradas
indice = object1.obtener_indice()
data = object1.obtener_data(indice[0][0])
data = object1.text_To_Columns(data)
object1.write_pandas_xlsx_document(data, 'nuevodocmnetiss.xlsx')
print(encontrados)
print(type(indice))
#print(data)

'''

#Hacer una instancia de la clase
instanca_Data = pr.PerformancePandas(name_Workwook, name_Sheet)

#Buscar todas las tablas necesarias, las siguientes lineas regresan solo las estadisticas de las coincidencias encontradas
#luego de hacer cada busqueda se obtine el indice de las coincidencias
#el siguiente paso es obtener los datos
#transformar de texto a columnas
'''wos host'''
encontrados_wos = instanca_Data.busqueda('WOS HOST')
indice = instanca_Data.obtener_indice()
data_wos = instanca_Data.obtener_data(indice[0][0] + 2) #al indice le sumamos 2 para evitar poner el nombre de la tabla y la linea que separa al nombre de los datos
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
dictionary_wos = instanca_Data.convert_to_directory(data_wos[:,1], data_wos[:,0])
dictionary_complete = instanca_Data.convert_to_directory(data_complete[:,1], data_complete[:,0])
dictionary_failed = instanca_Data.convert_to_directory(data_failed[:,1], data_failed[:,0])
dictionary_timeout = instanca_Data.convert_to_directory(data_timeout[:,1], data_timeout[:,0])

#podemos sacar los archivos correspondientes a las tablas encontradas
instanca_Data.write_pandas_xlsx_document_dictionary(dictionary_wos, 'wosJAmu.xlsx')
'''+*******************ESTA pendiente la linea anterior********************'''



#Luego que estan los diccionarios hay que alinear los vectores

data_wos, data_complete = instanca_Data.alignment(data_wos[:,1], data_complete[:,1])
data_wos, data_failed = instanca_Data.alignment(data_wos, data_failed[:,1])
data_wos, data_timeout = instanca_Data.alignment(data_wos, data_timeout[:,1])


#crear cada una de las matrices individuales
completed_Matrix = instanca_Data.create_Matrix_Excel(data_wos, data_complete, dictionary_wos, dictionary_complete)
failed_Matrix = instanca_Data.create_Matrix_Excel(data_wos, data_failed, dictionary_wos, dictionary_failed)
timeout_Matrix = instanca_Data.create_Matrix_Excel(data_wos, data_timeout, dictionary_wos, dictionary_timeout)

#Crear la matriz completa
full_Matrix = []
for i in range(len(data_wos)):
    full_Matrix.append(
        completed_Matrix[i] + failed_Matrix[i][2:] + timeout_Matrix[i][2:])


#escribir el archivo de excel
instanca_Data.write_pandas_xlsx_document(full_Matrix, 'pandas.xlsx')
'''
faileddetailed_count = instanca_Data.busqueda('FAILEDDETAILED')
timeoutdetailed_count = instanca_Data.busqueda('TIMEOUTDETAILED')


print('Estadisticas encontradas: \n')
print('\nWOS HOST: ', wos_host)
print('\nCOMPLETE: ', complete_count)
print('\nFAILED', faileddetailed_count)
print('\nTIMEOUT', timeoutdetailed_count)
'''
