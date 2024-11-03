immutable_var = 1, 2, 'cat', 'dog'
print(immutable_var)

#immutable_var[2]= 'chicken'
#print(immutable_var)            # элементы кортежа неизменны

mutable_list = [1, 2, 3, 'cat', 'dog']
print(mutable_list)

mutable_list.append('chicken')
print(mutable_list)

mutable_list.extend('fish')
print(mutable_list)

mutable_list.extend(['fish', 4])
print(mutable_list)

mutable_list.remove(4)
print(mutable_list)

mutable_list[3] = 'snake'
print(mutable_list)

print(mutable_list[0:5:2])