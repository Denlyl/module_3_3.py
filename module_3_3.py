def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [10, 'mother', True]
values_dict = {'a' : 15, 'b' : 'father', 'c' : False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [322, 'grandmother']
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)