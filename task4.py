# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

x = 10
y = 15
z = 2
print ("Наибольшее число", max(x,y,z))

# Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130

a = int(input())
b = int(input())
c = int(input())
list = [a,b,c]
print (list)
max_num = list[0]
print (max_num)

for num in list:
    if num > max_num:
        max_num = num
print ("Наибольшее число", max_num)
# Задачу решить без функций max и прочих.
# Значение переменных может меняться