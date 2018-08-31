name_Workwook = 'FLOW Operation and support report ASAP 7.0.2 JAMU66%2c WASS133 2018-08-27.xlsx'
name_Sheet = 'wass week'

import pandas as pd
import numpy as np
rango = 1776 - 1601
x = pd.read_excel(name_Workwook, sheet_name=name_Sheet,
                  usecols='A', skiprows=(1599), nrows=rango)

x = np.array(x)

matrix = np.array([x[i][0].split() for i in range(len(x))])


def f(mat):
    matr = []
    for i in range(len(mat)):
        try:
            int(mat[i][0])
            matr.append(mat[i][:])
        except:
            pass
    matr = np.array(matr)
    return matr


matrix = f(matrix)


''' clasificacion '''
#null
nullWass = []
accountWass = []
for i in range(len(matrix)):
    if 'NULL' in matrix[i][:]:
        nullWass.append(matrix[i])
        matrix[i] = None
    else:
        accountWass.append(matrix[i])
        matrix[i] = None

null_513 = []
null_520 = []
null_another = []
for i in range(len(nullWass)):
    if '513' in nullWass[i]:
        null_513.append(nullWass[i])
        nullWass[i] = None
    elif '520' in nullWass[i]:
        null_520.append(nullWass[i])
        nullWass[i] = None
    else:
        null_another.append(nullWass[i])
        nullWass[i] = None


account_513 = []
account_520 = []
account_another = []
for i in range(len(accountWass)):
    if '513' in accountWass[i]:
        account_513.append(accountWass[i])
        accountWass[i] = None
    elif '520' in accountWass[i]:
        account_520.append(accountWass[i])
        accountWass[i] = None
    else:
        account_another.append(accountWass[i])
        accountWass[i] = None

print('----------full matrix wassss---------', matrix, len(matrix))
print('----------null wassss---------', nullWass, len(nullWass))
print('-----------account wass-----', accountWass, len(accountWass))

excel_null_513 = pd.DataFrame(null_513)
excel_null_520 = pd.DataFrame(null_520)
excel_null_another = pd.DataFrame(null_another)
excel_account_513 = pd.DataFrame(account_513)
excel_account_520 = pd.DataFrame(account_520)
excel_account_another = pd.DataFrame(account_another)

excel_null_513.to_excel('null_513.xlsx')
excel_null_520.to_excel('nul_520.xlsx')
excel_null_another.to_excel('null_another.xlsx')
excel_account_513.to_excel('account_513.xlsx')
excel_account_520.to_excel('account_520.xlsx')
excel_account_another.to_excel('account_another.xlsx')
