import Performance as Pfce 

name_Workwook = 'FLOW Operation and support report ASAP 7.0.2 JAMU66%2c WASS133 2018-09-10.xlsx'
name_Sheet = 'WASS WEEK'

'''instancia'''
object1 = Pfce.Performance(name_Workwook, name_Sheet)


'''obtencion de datos, function Text to Columns'''
wos_host_data = object1.text_To_Columns('A2009', 'A2072')
completed_data = object1.text_To_Columns('A1961', 'A2003')
failed_data = object1.text_To_Columns('A1908', 'A1955')
timeout_data = object1.text_To_Columns('A28', 'A43')


'''conversion a diccionarios'''
wos_host_dic = object1.convert_to_directory(wos_host_data[:,1], wos_host_data[:,0])
completed_dic = object1.convert_to_directory(completed_data[:,1], completed_data[:,0])
failed_dic = object1.convert_to_directory(failed_data[:,1], failed_data[:,0])
timout_dic = object1.convert_to_directory(timeout_data[:,1], timeout_data[:,0])

'''--------generate the failed and timeout details section -------'''

object1.write_xlsx_Document(object1.dictionary_to_pyMatrix(failed_dic), 'WASS-FailedDetails.xlsx')
object1.write_xlsx_Document(object1.dictionary_to_pyMatrix(timout_dic), 'WASS-TimeoutDetails.xlsx')



'''------------------ALINEAMIENTO------------------------'''
wos_host_listA, completed_listA = object1.alignment(wos_host_data[:,1], completed_data[:,1])
wos_host_listA, failed_listA = object1.alignment(wos_host_data[:,1], failed_data[:,1])
wos_host_listA, timeout_listA = object1.alignment(wos_host_data[:,1], timeout_data[:,1])


'''create matrixes of Excel'''

completed_Matrix = object1.create_Matrix_Excel(wos_host_listA, completed_listA, wos_host_dic, completed_dic)
failed_Matrix = object1.create_Matrix_Excel(wos_host_listA, failed_listA, wos_host_dic, failed_dic)
timeout_Matrix = object1.create_Matrix_Excel(wos_host_listA, timeout_listA, wos_host_dic, timout_dic)

''' create full matrix '''

full_Matrix = []
for i in range(len(wos_host_listA)):
    full_Matrix.append(completed_Matrix[i] + failed_Matrix[i][2:] + timeout_Matrix[i][2:])

''' Write xlsx document '''
object1.write_xlsx_Document(full_Matrix, 'PerformanceWASS.xlsx')

