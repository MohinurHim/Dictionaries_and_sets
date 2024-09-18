my_dict ={'length':'m', 'time':'hour', 'power':'N'}
print(my_dict)
print(my_dict.get('length',))
print(my_dict.get('weight','kg'))
my_dict.update({'energy':'J','frequency':'Hz'})
print(my_dict)
a = my_dict.pop('energy')
print(a)
my_set = {24,45,45,24,True,'word',25,'word'}
print(my_set)
my_set.update(['string','time'])
print(my_set)
print(my_set.remove('word'))
print(my_set)