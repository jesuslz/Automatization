def convert_to_dictionary(list_1, list_2):
    '''Esta funcion convierte dos listas con las
    mismas dimensiones a un diccionario
    la lista 1 corresponde a las keys
    la lista 2 corresponde a los valores'''
    
    dictionary = dict(zip(list_1, list_2))

    return dictionary

'''
https://stackoverflow.com/questions/209840/convert-two-lists-into-a-dictionary-in-python
'''
