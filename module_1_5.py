# переменной присвоен кортеж с данными int, str, float, list, tup
immutable_var = [(1, 2, 3, 'Hello hell', 3.14,(1, 2, 3, "Hello hell", 3.14),[1, "Hello hell", 3.14])]

print(immutable_var)
# проверяем типы переменных
immutable_var_1 = 1, 2, 3                         #<class 'tuple'
immutable_var_2 = 'Hello hell'                    #<class 'str'>
immutable_var_3 = (1, 2, 3, "Hello hell", 3.14)   #<class 'tuple'>
immutable_var_4 = [1, "Hello hell", 3.14]         #<class 'list'>

print(type(immutable_var_1))
print(type(immutable_var_2))
print(type(immutable_var_3))
print(type(immutable_var_4))

# проверка индексации кортежа, вывод индекса [0] и для immutable_var_3 [3]

immutable_var = [(1, 2, 3, 'Hello hell', 3.14,(1, 2, 3, "Hello hell", 3.14),[1, "Hello hell", 3.14])]
immutable_var_3 = (1, 2, 3, "Hello hell", 3.14)
print(immutable_var[0])
print(immutable_var_3[3])

# Создание изменяемых структур данных
mutable_var =  [1, "Hello hell", 3.14]
mutable_var[1] = 'Paradise'
print(mutable_var)

# замена элемента в кортеже приводит к ошибке
immutable_var_3 = (1, 2, 3, "Hello hell", 3.14)
immutable_var_3[3] = 'Paradise'                     #TypeError: 'tuple' object does not support item assignment
print(immutable_var_3)
