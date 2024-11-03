my_dict = {'cat': 112233, 'dog': 112244, 'snake': 112255}
print(my_dict)
print(my_dict.get('cat'))
print(my_dict.get('elephant', 'не существует в словаре'))
my_dict['fish']=112266
print(my_dict)
my_dict.update({'cow':112277, 'fox':112288})
print(my_dict)
#del my_dict['cat']
#print(my_dict)
#my_dict.pop('cat')
#print(my_dict)
a=my_dict.pop('cat')
print(a)
print(my_dict)


my_set = {1, 2, 3, 4, 5, 2, 3, 5, 'cat', 'dog', 'cat'}
print(my_set)
my_set.update([6,7,'fish'])
print(my_set)

print(my_set.remove(1))
print(my_set)