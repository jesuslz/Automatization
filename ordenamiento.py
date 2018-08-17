
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
    'FLOW Operation and support report ASAP 7.0.2 JAMU66, WASS133 2018-08-13.xlsx', data_only=True)
sheet = file_xlsx['week jamu']
#print(y)

wos_host = np.array(list(sheet['A678':'A735']))
wos_host_data = [[wos_host[i][j].value for j in range(
    wos_host.shape[1])]for i in range(wos_host.shape[0])]

wos_host_x = np.array([wos_host_data[i][0].split()
                       for i in range(len(wos_host_data))])

failed = np.array(list(sheet['A632':'A672']))
failed = [[failed[i][j].value for j in range(failed.shape[1])] for i in range(failed.shape[0])]
failed_x = np.array([failed[i][0].split() for i in range(len(failed))])

wos_host_list = list(wos_host_x[:,1])
failed_list = list(failed_x[:,1])


wos_host_list, failed_list = alignment(wos_host_list, failed_list)

print('Wos' + '\t' + 'failed' + '\n')
for i in range(len(wos_host_list)):
    print(str(wos_host_list[i]) + '\t' + str(failed_list[i]) + '\n')

import dictionary as dic 

wos_hostDatos = list(wos_host_x[:, 0])
failedDatos = list(failed_x[:,0])

d2 = [list((int(wos_hostDatos[i]), wos_host_list[i])) for i in range(len(wos_host_list))]
#d1 = list(np.column_stack((wos_hostDatos, wos_host_list)))
#d2 = [list(d1[i][:]) for i in range(len(d1))]

print(d2)
#print(d2)
import escritura
#print(list(failed_x))
escritura.write_xlsx_document(d2, 'failed.xlsx')
