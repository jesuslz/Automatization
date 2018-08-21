'''
http://zetcode.com/articles/openpyxl/

'''
from openpyxl import Workbook

def write_xlsx_document(matrix_data, file_name):

    book = Workbook()
    sheet = book.active
    
    for row in matrix_data:
        sheet.append(row)
        #print(row)

    book.save(file_name)


