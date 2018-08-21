
import openpyxl
import numpy as np

def alignment(a, b):
    '''El primer parametro de esta funcion siempre debe ser
    el vector base'''
    a.sort()
    b.sort()
    #hacerlos del mismo tamaño
    for i in range(len(a)-len(b)):
        b.append(None)
        
    for i in range(len(a)):
        if not a[i] == b[i]:
            b.insert(i, None)
            b.pop(-1)

    return a, b



file_xlsx = openpyxl.load_workbook(
    'FLOW Operation and support report ASAP 7.0.2 JAMU66%2c WASS133 2018-08-20.xlsx', data_only=True)
sheet = file_xlsx['JAMU WEEK']
#print(y)

'''------WOS_HOST----------------------------'''
wos_host = np.array(list(sheet['A439':'A483']))
wos_host_data = [[wos_host[i][j].value for j in range(
    wos_host.shape[1])]for i in range(wos_host.shape[0])]

wos_host_x = np.array([wos_host_data[i][0].split()
                       for i in range(len(wos_host_data))])


'''-------COMPLETE-------------------------------'''
complete = np.array(list(sheet['A399':'A433']))
complete_data = [[complete[i][j].value for j in range(
    complete.shape[1])]for i in range(complete.shape[0])]

complete_x = np.array([complete_data[i][0].split()
                       for i in range(len(complete_data))])

'''---------------FAILED------------'''

failed = np.array(list(sheet['A358':'A392']))
failed = [[failed[i][j].value for j in range(failed.shape[1])] for i in range(failed.shape[0])]
failed_x = np.array([failed[i][0].split() for i in range(len(failed))])

'''--------------TIMEOUT-----------'''
timeout = np.array(list(sheet['A28':'A31']))
timeout = [[timeout[i][j].value for j in range(
    timeout.shape[1])] for i in range(timeout.shape[0])]
timeout_x = np.array([timeout[i][0].split() for i in range(len(timeout))])


'''---------------CONVERTIR A LISTAS-------------------'''
wos_host_list = list(wos_host_x[:, 1])
complete_list = list(complete_x[:, 1])
failed_list = list(failed_x[:, 1])
timeout_list = list(timeout_x[:, 1])


wos_host_Datos = list(wos_host_x[:, 0])
complete_Datos = list(complete_x[:, 0])
failed_Datos = list(failed_x[:, 0])
timeout_Datos = list(timeout_x[:, 0])

'''--------------CONVERTIR A DICCIONARIOS--------------'''
import dictionary

wos_host_dic = dictionary.convert_to_dictionary(wos_host_x[:,1], wos_host_x[:,0])
complete_dic = dictionary.convert_to_dictionary(
    complete_x[:, 1], complete_x[:, 0])
failed_dic = dictionary.convert_to_dictionary(failed_x[:,1], failed_x[:,0])

timeout_dic = dictionary.convert_to_dictionary(timeout_x[:, 1], timeout_x[:, 0])

'''------------------ALINEAMIENTO------------------------'''
wos_host_listA, complete_listA = alignment(wos_host_list, complete_list.copy())
wos_host_listA, failed_listA = alignment(wos_host_list, failed_list.copy())
wos_host_listA, timeout_listA = alignment(wos_host_list, timeout_list.copy())

'''
print('Wos' + '\t' + 'failed' + '\n')
for i in range(len(wos_host_list)):
    print(str(wos_host_list[i]) + '\t' + str(failed_list[i]) + '\n')
'''

'''------Escritura-------'''
d1 = []
for i in range(len(wos_host_listA)):
    try:
        d1.append(list((int(wos_host_dic[wos_host_listA[i]]),
                       wos_host_listA[i],
                       int(complete_dic[wos_host_listA[i]]),
                       complete_listA[i])))
    except:
        d1.append(list((int(wos_host_dic[wos_host_listA[i]]),
                       wos_host_listA[i], None, None)))

d2 = []
for i in range(len(wos_host_listA)):
    try:
        d2.append(list((int(wos_host_dic[wos_host_listA[i]]),
                       wos_host_listA[i],
                       int(failed_dic[wos_host_listA[i]]),
                       failed_listA[i])))
    except:
        d2.append(list((int(wos_host_dic[wos_host_listA[i]]),
                       wos_host_listA[i], None, None)))

d3 = []
for i in range(len(wos_host_listA)):
    try:
        d3.append(list((int(wos_host_dic[wos_host_listA[i]]),
                       wos_host_listA[i],
                       int(timeout_dic[wos_host_listA[i]]),
                       timeout_listA[i])))
    except:
        d3.append(list((int(wos_host_dic[wos_host_listA[i]]),
                       wos_host_listA[i], None, None)))


'''
for i in range(len(wos_host_listA)):
    try:
        d.append(list((int(wos_host_dic[wos_host_listA[i]]), 
                wos_host_listA[i], 
                int(complete_dic[wos_host_listA[i]]), 
                complete_listA[i], 
                int(failed_dic[wos_host_listA[i]]), 
                failed_listA[i], 
                int(timeout_dic[wos_host_listA[i]]), 
                timeout_listA[i])))
    except:
        d.append(list((int(wos_host_dic[wos_host_listA[i]]), wos_host_listA[i], None, None, None, None, None, None)))
    
'''
d = []
for i in range(len(wos_host_listA)):
    d.append(d1[i] + d2[i] + d3[i])
#d2 = [list((int(wos_host_Datos[i]), wos_host_list[i], complete_listA[i])) for i in range(len(wos_host_list))]
#d3 = [list((int(complete_Datos[i]), complete_list[i]))
#      for i in range(len(complete_list))]
#d4 = [list((int(failed_Datos[i]), failed_list[i]))
#      for i in range(len(failed_list))]
#d5 = [list((int(timeout_Datos[i]), timeout_list[i]))
#      for i in range(len(timeout_list))]
#d1 = list(np.column_stack((wos_hostDatos, wos_host_list)))
#d2 = [list(d1[i][:]) for i in range(len(d1))]


print(d)
import escritura
#print(list(failed_x))
escritura.write_xlsx_document(d, 'performanceJAMU.xlsx')
#escritura.write_xlsx_document(d2, 'failed.xlsx')
#escritura.write_xlsx_document(d3, 'timeout.xlsx')

