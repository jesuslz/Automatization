def dictionary_to_list(dic):
    list_keys = []
    list_values = []
    both_lists = []

    for keys, values in dic.items():
        list_keys.append(keys)
        list_values.append(values)
        both_lists.append(list((keys, values)))

    return list_keys, list_values, both_lists


dictionary = {'jamu1':1, 'jamu2':2, 'jamu3':1}
a, b, c = dictionary_to_list(dictionary)
print(a,b,c)
print(dictionary['jamu3'])
a = [None, None, 1, 2]
b = [None, None, 'jamu', 'was']
import dictionary

d1 = dictionary.convert_to_dictionary(b, a)

print(c)
