#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

my_list =list(map(int,input('Введите 10 чисел через пробел').split()))
if len(my_list) != 10:
    print ('Ошибка, нужно 10 чисел')
else:
    print (f'Ваш массив: {my_list}')

new_list = []
for i in my_list:
    new_list.append(i+1)
print(new_list)